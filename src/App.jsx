import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import { InterviewProvider } from './context/InterviewContext';
import HomePage from './pages/HomePage';
import JobRoleSelection from './pages/JobRoleSelection';
import RoundPage from './pages/RoundPage';
import EvaluationPage from './pages/EvaluationPage';

/**
 * Main App Component
 * Handles routing for the multi-page interview flow:
 * - Home Page (/)
 * - Job Role Selection (/job-selection)
 * - Round 1 - Screening (/round/1)
 * - Round 2 - Technical (/round/2)
 * - Round 3 - Scenario (/round/3)
 * - Final Evaluation (/evaluation)
 */
function App() {
  return (
    <ThemeProvider>
      <InterviewProvider>
        <Router>
          <Routes>
            {/* Home Page - Entry point */}
            <Route path="/" element={<HomePage />} />
            
            {/* Job Role Selection Page */}
            <Route path="/job-selection" element={<JobRoleSelection />} />
            
            {/* Round Pages - Dynamic route for all three rounds */}
            <Route path="/round/:roundId" element={<RoundPage />} />
            
            {/* Final Evaluation Page */}
            <Route path="/evaluation" element={<EvaluationPage />} />
            
            {/* Catch-all redirect to home */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </Router>
      </InterviewProvider>
    </ThemeProvider>
  );
}

export default App;
