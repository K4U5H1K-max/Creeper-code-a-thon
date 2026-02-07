import React, { createContext, useContext, useState, useCallback } from 'react';
import { interviewAPI } from '../services/api';

/**
 * InterviewContext
 * Manages the entire interview session state and API interactions
 */
const InterviewContext = createContext();

/**
 * Hook to use the Interview Context
 * @throws {Error} if used outside of InterviewProvider
 */
export const useInterview = () => {
  const context = useContext(InterviewContext);
  if (!context) {
    throw new Error('useInterview must be used within an InterviewProvider');
  }
  return context;
};

/**
 * InterviewProvider Component
 * Wraps the application and provides interview state and methods
 */
export const InterviewProvider = ({ children }) => {
  // Session state
  const [sessionId, setSessionId] = useState(null);
  const [jobRole, setJobRole] = useState('');
  const [candidateName, setCandidateName] = useState(null);
  
  // Round state
  const [currentRound, setCurrentRound] = useState(1);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [totalQuestions, setTotalQuestions] = useState(0);
  const [roundName, setRoundName] = useState('Screening Round');
  
  // Messages state
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  
  // Interview completion state
  const [interviewComplete, setInterviewComplete] = useState(false);
  const [roundComplete, setRoundComplete] = useState(false);
  const [roundPassed, setRoundPassed] = useState(null);
  const [roundFeedback, setRoundFeedback] = useState(null);
  const [finalEvaluation, setFinalEvaluation] = useState(null);

  /**
   * Start a new interview session
   * @param {string} role - Job role for the interview
   * @param {string|null} name - Optional candidate name
   */
  const startInterview = useCallback(async (role, name = null) => {
    try {
      setIsLoading(true);
      setError(null);
      
      const response = await interviewAPI.startInterview(role, name);
      
      // Update state
      setSessionId(response.session_id);
      setJobRole(response.job_role);
      setCandidateName(name);
      setCurrentRound(response.current_round);
      setTotalQuestions(response.total_questions);
      setRoundName(response.round_name);
      setCurrentQuestion(1);
      
      // Add AI greeting as first message
      const aiMessage = {
        id: 1,
        sender: 'ai',
        text: response.greeting,
        timestamp: new Date(),
        round: response.current_round
      };
      setMessages([aiMessage]);
      
      return response;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, []);

  /**
   * Send a message in the interview
   * @param {string} messageText - User's message
   */
  const sendMessage = useCallback(async (messageText) => {
    if (!sessionId || !messageText.trim()) return;

    try {
      setIsLoading(true);
      setError(null);
      
      // Add user message immediately
      const userMessage = {
        id: messages.length + 1,
        sender: 'user',
        text: messageText.trim(),
        timestamp: new Date(),
        round: currentRound
      };
      setMessages(prev => [...prev, userMessage]);

      // Send to backend
      const response = await interviewAPI.sendMessage(sessionId, messageText.trim());
      
      // Add AI response
      const aiMessage = {
        id: messages.length + 2,
        sender: 'ai',
        text: response.ai_message,
        timestamp: new Date(),
        round: response.current_round
      };
      setMessages(prev => [...prev, aiMessage]);

      // Update round state
      setCurrentRound(response.current_round);
      setCurrentQuestion(response.current_question + 1); // +1 for display (1-indexed)
      setTotalQuestions(response.total_questions);
      
      // Handle round completion
      if (response.round_complete) {
        setRoundComplete(true);
        setRoundPassed(response.round_passed);
        setRoundFeedback(response.round_feedback);
      } else {
        setRoundComplete(false);
      }

      // Handle interview completion
      if (response.interview_complete) {
        setInterviewComplete(true);
        if (response.final_evaluation) {
          setFinalEvaluation(response.final_evaluation);
        }
      }

      return response;
    } catch (err) {
      setError(err.message);
      
      // Add error message to chat
      const errorMessage = {
        id: messages.length + 2,
        sender: 'ai',
        text: '❌ Sorry, there was an error processing your message. Please try again.',
        timestamp: new Date(),
        round: currentRound,
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
      
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, [sessionId, messages, currentRound]);

  /**
   * Reset the interview to start over
   */
  const resetInterview = useCallback(() => {
    setSessionId(null);
    setJobRole('');
    setCandidateName(null);
    setCurrentRound(1);
    setCurrentQuestion(0);
    setTotalQuestions(0);
    setRoundName('Screening Round');
    setMessages([]);
    setIsLoading(false);
    setError(null);
    setInterviewComplete(false);
    setRoundComplete(false);
    setRoundPassed(null);
    setRoundFeedback(null);
    setFinalEvaluation(null);
  }, []);

  /**
   * Get round information
   */
  const getRoundInfo = useCallback(() => {
    const rounds = [
      { 
        id: 1, 
        name: 'Screening', 
        description: 'Initial screening to assess basic qualifications and fit',
        questions: 4
      },
      { 
        id: 2, 
        name: 'Technical', 
        description: 'Deep technical assessment of skills and knowledge',
        questions: 5
      },
      { 
        id: 3, 
        name: 'Scenario', 
        description: 'Real-world problem-solving and decision-making scenarios',
        questions: 3
      }
    ];
    
    return rounds.find(r => r.id === currentRound) || rounds[0];
  }, [currentRound]);

  const value = {
    // Session state
    sessionId,
    jobRole,
    candidateName,
    
    // Round state
    currentRound,
    currentQuestion,
    totalQuestions,
    roundName,
    
    // Messages
    messages,
    isLoading,
    error,
    
    // Completion state
    interviewComplete,
    roundComplete,
    roundPassed,
    roundFeedback,
    finalEvaluation,
    
    // Methods
    startInterview,
    sendMessage,
    resetInterview,
    getRoundInfo
  };

  return (
    <InterviewContext.Provider value={value}>
      {children}
    </InterviewContext.Provider>
  );
};

export default InterviewContext;
