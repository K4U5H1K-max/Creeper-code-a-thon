"""
Groq API service for handling AI interactions.
"""

import os
from typing import List, Dict
from groq import Groq
from models import Message

class GroqService:
    """Service for interacting with Groq API."""
    
    # Different models for each round to add variety
    ROUND_MODELS = {
        1: "llama-3.3-70b-versatile",      # Screening - versatile model
        2: "llama-3.3-70b-versatile",      # Technical - powerful for technical content
        3: "llama-3.3-70b-versatile"       # Scenario - versatile for complex scenarios
    }
    
    def __init__(self, api_key: str):
        """Initialize the Groq service with API key."""
        self.client = Groq(api_key=api_key)
        self.default_model = "llama-3.3-70b-versatile"
    
    def get_model_for_round(self, round_number: int) -> str:
        """Get the appropriate model for a specific round."""
        return self.ROUND_MODELS.get(round_number, self.default_model)
    
    def chat_completion(
        self, 
        messages: List[Dict[str, str]], 
        round_number: int = 1,
        temperature: float = 0.7,
        max_tokens: int = 1024
    ) -> str:
        """
        Get a chat completion from Groq API.
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            round_number: Current interview round (determines model)
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens in response
            
        Returns:
            AI response content as string
        """
        try:
            model = self.get_model_for_round(round_number)
            
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=1,
                stream=False
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Error in Groq API call: {str(e)}")
            raise Exception(f"Failed to get AI response: {str(e)}")
    
    def generate_greeting(self, job_role: str, round_number: int, round_info: Dict) -> str:
        """
        Generate an initial greeting and round explanation.
        
        Args:
            job_role: The job role being interviewed for
            round_number: Current round number
            round_info: Information about the round
            
        Returns:
            Greeting message from AI
        """
        if round_number == 1:
            prompt = f"""You are starting an interview for a {job_role} position. 
            
            Greet the candidate warmly and professionally. Then explain that this is Round 1: {round_info['name']}.
            
            Briefly explain:
            - This is the {round_info['name']}
            - Purpose: {round_info['description']}
            - You will ask {round_info['questions_count']} questions
            - Focus areas: {', '.join(round_info['focus_areas'])}
            
            Keep it concise and encouraging. End by asking the first question about their background and experience with {job_role}.
            
            Do NOT use phrases like "Question 1/4" - integrate it naturally into your conversation."""
            
        else:
            prompt = f"""The candidate has passed Round {round_number - 1}. Congratulate them briefly and introduce Round {round_number}: {round_info['name']}.
            
            Explain:
            - This is Round {round_number}: {round_info['name']}
            - Purpose: {round_info['description']}
            - You will ask {round_info['questions_count']} questions
            - Focus areas: {', '.join(round_info['focus_areas'])}
            
            Keep it professional and set the right tone for this round. End by asking the first question relevant to a {job_role} role.
            
            Do NOT use phrases like "Question 1/{round_info['questions_count']}" - integrate it naturally."""
        
        messages = [
            {"role": "system", "content": "You are a professional interviewer. Be warm, clear, and concise."},
            {"role": "user", "content": prompt}
        ]
        
        return self.chat_completion(messages, round_number, temperature=0.8)
    
    def ask_next_question(
        self, 
        conversation_history: List[Message],
        system_prompt: str,
        round_number: int,
        current_question: int,
        total_questions: int
    ) -> str:
        """
        Ask the next question based on conversation history.
        
        Args:
            conversation_history: Previous messages in the interview
            system_prompt: System prompt for the current round
            round_number: Current round number
            current_question: Current question number (0-indexed)
            total_questions: Total questions in this round
            
        Returns:
            Next question from AI
        """
        # Convert Message objects to dict format for API
        messages = [{"role": "system", "content": system_prompt}]
        
        for msg in conversation_history:
            if msg.role in ["user", "assistant"]:
                messages.append({"role": msg.role, "content": msg.content})
        
        # Add instruction for next question
        next_q_num = current_question + 1
        instruction = f"""Based on the conversation so far, ask question {next_q_num} out of {total_questions}. 
        
        Make it relevant to the previous responses. Do NOT explicitly state "Question {next_q_num}/{total_questions}" - keep it conversational and natural.
        
        Ask only ONE question and wait for the response."""
        
        messages.append({"role": "user", "content": instruction})
        
        return self.chat_completion(messages, round_number, temperature=0.75, max_tokens=512)
    
    def evaluate_answer(
        self,
        conversation_history: List[Message],
        system_prompt: str,
        round_number: int,
        is_last_question: bool
    ) -> str:
        """
        Evaluate the candidate's answer and provide feedback.
        
        Args:
            conversation_history: Previous messages in the interview
            system_prompt: System prompt for the current round
            round_number: Current round number
            is_last_question: Whether this is the last question in the round
            
        Returns:
            Feedback from AI
        """
        messages = [{"role": "system", "content": system_prompt}]
        
        for msg in conversation_history:
            if msg.role in ["user", "assistant"]:
                messages.append({"role": msg.role, "content": msg.content})
        
        if is_last_question:
            instruction = """Provide brief feedback on this answer. This was the last question in this round. 
            
            Thank them and let them know the round is complete. Keep it short and professional."""
        else:
            instruction = """Provide very brief feedback on this answer (1-2 sentences). 
            
            Acknowledge their response and prepare to move to the next question. Be encouraging but honest."""
        
        messages.append({"role": "user", "content": instruction})
        
        return self.chat_completion(messages, round_number, temperature=0.6, max_tokens=256)
