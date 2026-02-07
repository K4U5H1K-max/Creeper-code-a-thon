import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowRight } from 'lucide-react';
import { useInterview } from '../context/InterviewContext';

/**
 * JobRoleSelection Component
 * Simple, focused page for entering job role before interview
 * Features: Centered text input with inline proceed button
 */
const JobRoleSelection = () => {
  const navigate = useNavigate();
  const { startInterview } = useInterview();
  const [jobRole, setJobRole] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Handle proceed to screening round
   * Starts the interview via backend API
   */
  const handleProceed = async () => {
    if (jobRole.trim()) {
      try {
        setIsLoading(true);
        setError(null);
        
        // Start interview through backend
        await startInterview(jobRole.trim());
        
        // Navigate to first round
        navigate('/round/1');
      } catch (err) {
        setError('Failed to start interview. Please ensure the backend is running.');
        console.error('Error starting interview:', err);
      } finally {
        setIsLoading(false);
      }
    }
  };

  /**
   * Handle Enter key press to proceed
   */
  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && jobRole.trim() && !isLoading) {
      handleProceed();
    }
  };

  return (
    <div className="min-h-screen relative overflow-hidden">
      {/* Subtle Background Gradient */}
      <div className="absolute inset-0 bg-gradient-to-br from-neutral-50 via-slate-50 to-blue-50 dark:from-neutral-900 dark:via-neutral-900 dark:to-slate-900 transition-colors duration-200"></div>
      
      {/* Soft Abstract Background Pattern */}
      <div className="absolute inset-0 opacity-20 dark:opacity-5">
        <div className="absolute top-1/4 right-1/4 w-96 h-96 bg-blue-200 dark:bg-blue-800 rounded-full mix-blend-multiply filter blur-3xl"></div>
        <div className="absolute bottom-1/4 left-1/4 w-96 h-96 bg-purple-200 dark:bg-purple-800 rounded-full mix-blend-multiply filter blur-3xl"></div>
      </div>

      {/* Main Content - Centered Vertically and Horizontally */}
      <div className="relative z-10 min-h-screen flex items-center justify-center px-4">
        <div className="w-full max-w-3xl">
          
          {/* Main Input Card */}
          <div className="bg-white/90 dark:bg-neutral-800/90 backdrop-blur-md rounded-2xl shadow-2xl border border-neutral-200/50 dark:border-neutral-700/50 p-12 transition-colors duration-200">
            
            {/* Title Section */}
            <div className="text-center mb-10">
              <h1 className="text-3xl md:text-4xl font-bold text-neutral-900 dark:text-white mb-3">
                What role are you interviewing for?
              </h1>
              <p className="text-neutral-600 dark:text-neutral-400 text-lg">
                Let us know the position to tailor your interview experience
              </p>
            </div>

            {/* Input Container with Inline Button */}
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-4">
              
              {/* Text Input Field */}
              <input
                type="text"
                value={jobRole}
                onChange={(e) => setJobRole(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="e.g., Software Engineer, Data Scientist, Product Manager"
                disabled={isLoading}
                className="flex-1 px-6 py-4 text-lg border-2 border-neutral-300 dark:border-neutral-600 rounded-xl 
                          focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent 
                          bg-white dark:bg-neutral-900 text-neutral-900 dark:text-white 
                          placeholder-neutral-400 dark:placeholder-neutral-500
                          disabled:opacity-50 disabled:cursor-not-allowed
                          transition-all duration-200"
                autoFocus
              />

              {/* Proceed Button - Inline with Input */}
              <button
                onClick={handleProceed}
                disabled={!jobRole.trim() || isLoading}
                className={`
                  px-8 py-4 rounded-xl font-semibold text-lg flex items-center justify-center space-x-2
                  transition-all duration-300 shadow-lg min-w-[200px]
                  ${jobRole.trim() && !isLoading
                    ? 'bg-gradient-to-r from-primary-600 to-purple-600 text-white hover:from-primary-700 hover:to-purple-700 hover:shadow-xl transform hover:-translate-y-0.5 cursor-pointer'
                    : 'bg-neutral-300 dark:bg-neutral-700 text-neutral-500 dark:text-neutral-500 cursor-not-allowed opacity-60'
                  }
                `}
              >
                {isLoading ? (
                  <>
                    <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                    <span>Starting...</span>
                  </>
                ) : (
                  <>
                    <span className="whitespace-nowrap">Start Interview</span>
                    <ArrowRight className={`w-5 h-5 ${jobRole.trim() ? 'group-hover:translate-x-1' : ''} transition-transform`} />
                  </>
                )}
              </button>
            </div>

            {/* Error Message */}
            {error && (
              <div className="mt-4 p-4 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg">
                <p className="text-red-600 dark:text-red-400 text-sm">
                  ⚠️ {error}
                </p>
              </div>
            )}

            {/* Helper Text */}
            <p className="text-center text-sm text-neutral-500 dark:text-neutral-400 mt-6">
              Press Enter or click the button to continue
            </p>
          </div>

          {/* Footer Note */}
          <p className="text-center text-sm text-neutral-500 dark:text-neutral-400 mt-8">
            Example: Software Engineer, Product Manager, Data Analyst, etc.
          </p>
        </div>
      </div>
    </div>
  );
};

export default JobRoleSelection;
