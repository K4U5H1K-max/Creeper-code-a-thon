"""
Main Flask application for the multi-round interview system.
"""

import os
import uuid
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from typing import Dict

from models import (
    InterviewSession, RoundData, Message, QuestionAnswer,
    StartInterviewRequest, ChatRequest, ChatResponse
)
from groq_service import GroqService
from evaluator import InterviewEvaluator
from prompts import get_round_prompt, get_round_info

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Groq service
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")

groq_service = GroqService(GROQ_API_KEY)
evaluator = InterviewEvaluator()

# In-memory storage for active sessions (use database in production)
active_sessions: Dict[str, InterviewSession] = {}

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy", "service": "interview-backend"}), 200

@app.route('/api/start-interview', methods=['POST'])
def start_interview():
    """
    Start a new interview session.
    Expects: { "job_role": "string", "candidate_name": "string" (optional) }
    Returns: session details and initial greeting
    """
    try:
        data = request.get_json()
        req = StartInterviewRequest(**data)
        
        # Create new session
        session_id = str(uuid.uuid4())
        session = InterviewSession(
            session_id=session_id,
            job_role=req.job_role,
            candidate_name=req.candidate_name,
            current_round=1,
            current_question=0
        )
        
        # Initialize Round 1
        round_info = get_round_info(1)
        round_1 = RoundData(
            round_number=1,
            round_name=round_info['name'],
            status="in_progress"
        )
        session.rounds[1] = round_1
        
        # Generate initial greeting and first question
        greeting = groq_service.generate_greeting(req.job_role, 1, round_info)
        
        # Add to conversation history
        session.conversation_history.append(Message(
            role="assistant",
            content=greeting
        ))
        
        # Store session
        active_sessions[session_id] = session
        
        return jsonify({
            "session_id": session_id,
            "job_role": req.job_role,
            "current_round": 1,
            "round_name": round_info['name'],
            "greeting": greeting,
            "total_questions": round_info['questions_count']
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle chat messages during interview.
    Expects: { "session_id": "string", "message": "string" }
    Returns: AI response and session status
    """
    try:
        data = request.get_json()
        req = ChatRequest(**data)
        
        # Get session
        session = active_sessions.get(req.session_id)
        if not session:
            return jsonify({"error": "Session not found"}), 404
        
        if session.status != "active":
            return jsonify({"error": "Interview is not active"}), 400
        
        # Add user message to history
        session.conversation_history.append(Message(
            role="user",
            content=req.message
        ))
        
        current_round = session.current_round
        round_data = session.rounds[current_round]
        round_info = get_round_info(current_round)
        total_questions = round_info['questions_count']
        
        # Check if we're waiting for an answer
        if session.current_question < total_questions:
            # Process the answer
            question_idx = session.current_question
            
            # Get AI feedback on the answer
            system_prompt = get_round_prompt(current_round, session.job_role)
            is_last_question = (question_idx == total_questions - 1)
            
            feedback = groq_service.evaluate_answer(
                session.conversation_history,
                system_prompt,
                current_round,
                is_last_question
            )
            
            # Store Q&A
            last_question = (
                session.conversation_history[-3].content 
                if len(session.conversation_history) >= 3 
                else "Initial question"
            )
            
            qa = QuestionAnswer(
                question_number=question_idx + 1,
                question=last_question,
                answer=req.message,
                ai_feedback=feedback
            )
            
            # Calculate score for this question
            qa.score = evaluator.calculate_question_score(
                req.message, feedback, question_idx + 1, total_questions
            )
            
            round_data.questions.append(qa)
            
            # Add feedback to conversation
            session.conversation_history.append(Message(
                role="assistant",
                content=feedback
            ))
            
            # Move to next question
            session.current_question += 1
            
            # Check if round is complete
            if session.current_question >= total_questions:
                # Round complete - evaluate
                question_scores = [qa.score for qa in round_data.questions]
                round_score = evaluator.calculate_round_score(question_scores, current_round)
                round_data.round_score = round_score
                
                # Determine pass/fail
                passed, round_feedback = evaluator.determine_round_pass(round_score, current_round)
                round_data.passed = passed
                round_data.feedback = round_feedback
                round_data.status = "completed" if passed else "failed"
                
                if passed and current_round < 3:
                    # Move to next round
                    session.current_round += 1
                    session.current_question = 0
                    
                    # Initialize next round
                    next_round_info = get_round_info(session.current_round)
                    next_round = RoundData(
                        round_number=session.current_round,
                        round_name=next_round_info['name'],
                        status="in_progress"
                    )
                    session.rounds[session.current_round] = next_round
                    
                    # Generate greeting for next round
                    next_greeting = groq_service.generate_greeting(
                        session.job_role, 
                        session.current_round, 
                        next_round_info
                    )
                    
                    session.conversation_history.append(Message(
                        role="assistant",
                        content=f"\n\n{round_feedback}\n\n{next_greeting}"
                    ))
                    
                    response = ChatResponse(
                        session_id=session.session_id,
                        ai_message=f"{feedback}\n\n{round_feedback}\n\n{next_greeting}",
                        current_round=session.current_round,
                        current_question=0,
                        total_questions=next_round_info['questions_count'],
                        round_complete=True,
                        round_passed=True,
                        round_feedback=round_feedback
                    )
                    
                elif passed and current_round == 3:
                    # All rounds complete - final evaluation
                    round_scores = {
                        round_num: round_data.round_score 
                        for round_num, round_data in session.rounds.items()
                    }
                    final_eval = evaluator.calculate_final_evaluation(round_scores)
                    
                    session.final_evaluation = final_eval
                    session.status = "completed"
                    
                    final_message = f"""{feedback}

{round_feedback}

🎉 Congratulations! You've completed all three rounds of the interview.

Final Evaluation:
- Overall Score: {final_eval['overall_score']:.1f}%
- Confidence Score: {final_eval['confidence_score']:.1f}%
- Batch Assignment: {final_eval['batch']}
- Recommendation: {final_eval['recommendation']}

{final_eval['summary']}

Thank you for your time and effort in this interview process!"""
                    
                    session.conversation_history.append(Message(
                        role="assistant",
                        content=final_message
                    ))
                    
                    response = ChatResponse(
                        session_id=session.session_id,
                        ai_message=final_message,
                        current_round=current_round,
                        current_question=session.current_question,
                        total_questions=total_questions,
                        round_complete=True,
                        round_passed=True,
                        interview_complete=True,
                        round_feedback=round_feedback,
                        final_evaluation=final_eval
                    )
                    
                else:
                    # Failed round - interview terminated
                    session.status = "terminated"
                    
                    termination_message = f"""{feedback}

{round_feedback}

Unfortunately, you did not meet the requirements to proceed to the next round. 

Thank you for your time and interest. We encourage you to continue developing your skills and apply again in the future."""
                    
                    session.conversation_history.append(Message(
                        role="assistant",
                        content=termination_message
                    ))
                    
                    response = ChatResponse(
                        session_id=session.session_id,
                        ai_message=termination_message,
                        current_round=current_round,
                        current_question=session.current_question,
                        total_questions=total_questions,
                        round_complete=True,
                        round_passed=False,
                        interview_complete=True,
                        round_feedback=round_feedback
                    )
                
                return jsonify(response.dict()), 200
            
            else:
                # Ask next question
                next_question = groq_service.ask_next_question(
                    session.conversation_history,
                    system_prompt,
                    current_round,
                    session.current_question,
                    total_questions
                )
                
                session.conversation_history.append(Message(
                    role="assistant",
                    content=next_question
                ))
                
                response = ChatResponse(
                    session_id=session.session_id,
                    ai_message=f"{feedback}\n\n{next_question}",
                    current_round=current_round,
                    current_question=session.current_question,
                    total_questions=total_questions,
                    round_complete=False
                )
                
                return jsonify(response.dict()), 200
        
    except Exception as e:
        print(f"Error in chat: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/session/<session_id>', methods=['GET'])
def get_session(session_id: str):
    """Get current session status."""
    session = active_sessions.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404
    
    return jsonify(session.dict()), 200

@app.route('/api/session/<session_id>/history', methods=['GET'])
def get_conversation_history(session_id: str):
    """Get conversation history for a session."""
    session = active_sessions.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404
    
    return jsonify({
        "session_id": session_id,
        "history": [msg.dict() for msg in session.conversation_history]
    }), 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
