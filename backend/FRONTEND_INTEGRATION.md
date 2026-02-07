# Frontend Integration Guide

This guide shows how to integrate the React frontend with the Python backend.

## Backend API Integration

### 1. Create API Service File

Create `src/services/api.js`:

```javascript
const API_BASE_URL = 'http://localhost:5000/api';

export const interviewAPI = {
  // Start a new interview
  async startInterview(jobRole, candidateName = null) {
    const response = await fetch(`${API_BASE_URL}/start-interview`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        job_role: jobRole,
        candidate_name: candidateName
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to start interview');
    }
    
    return response.json();
  },

  // Send a chat message
  async sendMessage(sessionId, message) {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        session_id: sessionId,
        message: message
      })
    });
    
    if (!response.ok) {
      throw new Error('Failed to send message');
    }
    
    return response.json();
  },

  // Get session status
  async getSession(sessionId) {
    const response = await fetch(`${API_BASE_URL}/session/${sessionId}`);
    
    if (!response.ok) {
      throw new Error('Failed to get session');
    }
    
    return response.json();
  },

  // Get conversation history
  async getHistory(sessionId) {
    const response = await fetch(`${API_BASE_URL}/session/${sessionId}/history`);
    
    if (!response.ok) {
      throw new Error('Failed to get history');
    }
    
    return response.json();
  }
};
```

### 2. Update Interview Context

Create `src/context/InterviewContext.jsx`:

```javascript
import React, { createContext, useContext, useState } from 'react';
import { interviewAPI } from '../services/api';

const InterviewContext = createContext();

export function InterviewProvider({ children }) {
  const [sessionId, setSessionId] = useState(null);
  const [jobRole, setJobRole] = useState('');
  const [currentRound, setCurrentRound] = useState(1);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [totalQuestions, setTotalQuestions] = useState(0);
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [finalEvaluation, setFinalEvaluation] = useState(null);
  const [interviewComplete, setInterviewComplete] = useState(false);

  const startInterview = async (role, candidateName) => {
    try {
      setIsLoading(true);
      const response = await interviewAPI.startInterview(role, candidateName);
      
      setSessionId(response.session_id);
      setJobRole(response.job_role);
      setCurrentRound(response.current_round);
      setTotalQuestions(response.total_questions);
      setCurrentQuestion(1);
      
      // Add AI greeting to messages
      setMessages([{
        role: 'assistant',
        content: response.greeting,
        timestamp: new Date().toISOString()
      }]);
      
      return response;
    } catch (error) {
      console.error('Failed to start interview:', error);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const sendMessage = async (message) => {
    if (!sessionId || !message.trim()) return;

    try {
      setIsLoading(true);
      
      // Add user message
      const userMessage = {
        role: 'user',
        content: message,
        timestamp: new Date().toISOString()
      };
      setMessages(prev => [...prev, userMessage]);

      // Send to backend
      const response = await interviewAPI.sendMessage(sessionId, message);
      
      // Add AI response
      const aiMessage = {
        role: 'assistant',
        content: response.ai_message,
        timestamp: new Date().toISOString()
      };
      setMessages(prev => [...prev, aiMessage]);

      // Update state
      setCurrentRound(response.current_round);
      setCurrentQuestion(response.current_question);
      setTotalQuestions(response.total_questions);

      // Handle round/interview completion
      if (response.interview_complete) {
        setInterviewComplete(true);
        if (response.final_evaluation) {
          setFinalEvaluation(response.final_evaluation);
        }
      }

      return response;
    } catch (error) {
      console.error('Failed to send message:', error);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const resetInterview = () => {
    setSessionId(null);
    setJobRole('');
    setCurrentRound(1);
    setCurrentQuestion(0);
    setTotalQuestions(0);
    setMessages([]);
    setFinalEvaluation(null);
    setInterviewComplete(false);
  };

  return (
    <InterviewContext.Provider
      value={{
        sessionId,
        jobRole,
        currentRound,
        currentQuestion,
        totalQuestions,
        messages,
        isLoading,
        finalEvaluation,
        interviewComplete,
        startInterview,
        sendMessage,
        resetInterview
      }}
    >
      {children}
    </InterviewContext.Provider>
  );
}

export function useInterview() {
  const context = useContext(InterviewContext);
  if (!context) {
    throw new Error('useInterview must be used within InterviewProvider');
  }
  return context;
}
```

### 3. Update App.jsx

```javascript
import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import { InterviewProvider } from './context/InterviewContext';
import HomePage from './pages/HomePage';
import JobRoleSelection from './pages/JobRoleSelection';
import RoundPage from './pages/RoundPage';
import EvaluationPage from './pages/EvaluationPage';

function App() {
  return (
    <ThemeProvider>
      <InterviewProvider>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/select-role" element={<JobRoleSelection />} />
            <Route path="/interview" element={<RoundPage />} />
            <Route path="/evaluation" element={<EvaluationPage />} />
          </Routes>
        </BrowserRouter>
      </InterviewProvider>
    </ThemeProvider>
  );
}

export default App;
```

### 4. Update InterviewChat Component

```javascript
import React, { useState, useRef, useEffect } from 'react';
import { Send } from 'lucide-react';
import { useInterview } from '../context/InterviewContext';

export default function InterviewChat() {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);
  const { messages, isLoading, sendMessage } = useInterview();

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (input.trim() && !isLoading) {
      const message = input.trim();
      setInput('');
      await sendMessage(message);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex flex-col h-full">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[80%] rounded-lg p-4 ${
                msg.role === 'user'
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-gray-100'
              }`}
            >
              <p className="whitespace-pre-wrap">{msg.content}</p>
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-100 dark:bg-gray-800 rounded-lg p-4">
              <div className="flex space-x-2">
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-100" />
                <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce delay-200" />
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="border-t dark:border-gray-700 p-4">
        <div className="flex gap-2">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your answer..."
            className="flex-1 resize-none rounded-lg border border-gray-300 dark:border-gray-600 
                     bg-white dark:bg-gray-800 px-4 py-3 focus:outline-none focus:ring-2 
                     focus:ring-blue-500 dark:text-white"
            rows="2"
            disabled={isLoading}
          />
          <button
            onClick={handleSend}
            disabled={isLoading || !input.trim()}
            className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 
                     disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            <Send className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
}
```

### 5. Update ProgressStepper Component

```javascript
import React from 'react';
import { CheckCircle2, Circle } from 'lucide-react';
import { useInterview } from '../context/InterviewContext';

export default function ProgressStepper() {
  const { currentRound, currentQuestion, totalQuestions } = useInterview();

  const rounds = [
    { number: 1, name: 'Screening', questions: 4 },
    { number: 2, name: 'Technical', questions: 5 },
    { number: 3, name: 'Scenario', questions: 3 }
  ];

  return (
    <div className="space-y-4">
      {rounds.map((round) => {
        const isActive = round.number === currentRound;
        const isCompleted = round.number < currentRound;

        return (
          <div key={round.number} className="flex items-start gap-4">
            <div className="flex flex-col items-center">
              {isCompleted ? (
                <CheckCircle2 className="w-8 h-8 text-green-500" />
              ) : (
                <Circle
                  className={`w-8 h-8 ${
                    isActive ? 'text-blue-600' : 'text-gray-400'
                  }`}
                />
              )}
            </div>
            <div className="flex-1">
              <h3
                className={`font-semibold ${
                  isActive ? 'text-blue-600' : 'text-gray-600 dark:text-gray-400'
                }`}
              >
                Round {round.number}: {round.name}
              </h3>
              {isActive && (
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  Question {currentQuestion} of {totalQuestions}
                </p>
              )}
              {isCompleted && (
                <p className="text-sm text-green-600">Completed ✓</p>
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
}
```

## Testing the Integration

1. **Start Backend:**
```bash
cd backend
python app.py
```

2. **Start Frontend:**
```bash
npm run dev
```

3. **Test Flow:**
   - Select a job role
   - Start the interview
   - Answer questions
   - Complete all rounds
   - View final evaluation

## Environment Variables

Create `.env` in frontend root if needed:

```env
VITE_API_BASE_URL=http://localhost:5000/api
```

Then update `api.js`:

```javascript
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api';
```

## Error Handling

Add error boundaries and proper error handling:

```javascript
// In your components
try {
  await sendMessage(message);
} catch (error) {
  console.error('Error:', error);
  // Show error toast/notification to user
  alert('Failed to send message. Please try again.');
}
```

## Production Deployment

### Backend:
- Deploy to Heroku, Railway, or Render
- Set environment variables
- Use production WSGI server (gunicorn)

### Frontend:
- Update API_BASE_URL to production backend URL
- Build: `npm run build`
- Deploy to Vercel, Netlify, or similar

## Next Steps

1. ✅ Create the API service file
2. ✅ Set up Interview Context
3. ✅ Update components to use the context
4. ✅ Test the complete flow
5. ✅ Add error handling
6. ✅ Deploy to production
