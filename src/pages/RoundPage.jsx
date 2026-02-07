import React, { useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useInterview } from '../context/InterviewContext';
import Header from '../components/Header';
import ProgressStepper from '../components/ProgressStepper';
import InterviewChat from '../components/InterviewChat';
import ContextPanel from '../components/ContextPanel';

/**
 * RoundPage Component
 * Shared layout for all interview rounds (1, 2, 3)
 * Handles the interview conversation and progression
 * Connected to backend API via InterviewContext
 */
const RoundPage = () => {
  const { roundId } = useParams();
  const navigate = useNavigate();
  const requestedRound = parseInt(roundId);

  const {
    sessionId,
    currentRound,
    messages,
    sendMessage,
    interviewComplete,
    roundComplete,
    roundPassed,
    finalEvaluation
  } = useInterview();

  // Interview rounds configuration
  const rounds = [
    { 
      id: 1, 
      name: 'Screening', 
      description: 'Initial screening to assess basic qualifications and fit'
    },
    { 
      id: 2, 
      name: 'Technical', 
      description: 'Deep technical assessment of skills and knowledge'
    },
    { 
      id: 3, 
      name: 'Scenario', 
      description: 'Real-world problem-solving and decision-making scenarios'
    }
  ];

  // Redirect if no session
  useEffect(() => {
    if (!sessionId) {
      navigate('/job-selection');
    }
  }, [sessionId, navigate]);

  // Redirect if invalid round
  useEffect(() => {
    if (requestedRound < 1 || requestedRound > 3) {
      navigate('/');
    }
  }, [requestedRound, navigate]);

  // Handle interview completion - redirect to evaluation
  useEffect(() => {
    if (interviewComplete && finalEvaluation) {
      navigate('/evaluation');
    }
  }, [interviewComplete, finalEvaluation, navigate]);

  // Handle round completion - Check if failed
  useEffect(() => {
    if (roundComplete && roundPassed === false) {
      // Failed the round - interview terminated
      setTimeout(() => {
        navigate('/evaluation');
      }, 3000); // Give user time to read the failure message
    }
  }, [roundComplete, roundPassed, navigate]);

  // Handler for sending a new message
  const handleSendMessage = async (text) => {
    try {
      await sendMessage(text);
    } catch (err) {
      console.error('Failed to send message:', err);
    }
  };

  // Get current round info
  const currentRoundInfo = rounds[currentRound - 1] || rounds[0];

  if (!sessionId) {
    return null; // Will redirect
  }

  return (
    <div className="min-h-screen bg-neutral-50 dark:bg-neutral-900 transition-colors duration-200">
      {/* Main Header */}
      <Header status="Interview In Progress" />

      {/* Main Content Area */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        {/* Progress Stepper */}
        <div className="mb-6">
          <ProgressStepper 
            rounds={rounds}
            currentRound={currentRound}
          />
        </div>

        {/* Main Interview Area */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Chat Panel (Takes 2 columns on large screens) */}
          <div className="lg:col-span-2">
            <InterviewChat 
              messages={messages}
              currentRound={currentRound}
              onSendMessage={handleSendMessage}
              roundName={currentRoundInfo.name}
            />
          </div>

          {/* Context/Info Panel (Takes 1 column on large screens) */}
          <div className="lg:col-span-1">
            <ContextPanel 
              currentRound={currentRoundInfo}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default RoundPage;
