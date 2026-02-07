import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Briefcase, ArrowRight, CheckCircle2, Sparkles, Target, TrendingUp } from 'lucide-react';

/**
 * HomePage Component
 * Enhanced landing page for the interview platform
 * Features: Modern gradients, patterns, proper visual hierarchy
 */
const HomePage = () => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate('/job-selection');
  };

  return (
    <div className="min-h-screen relative overflow-hidden">
      {/* Animated Background with Gradients */}
      <div className="absolute inset-0 bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-neutral-900 dark:via-blue-900/20 dark:to-purple-900/20 transition-colors duration-200"></div>
      
      {/* Abstract Shapes Background */}
      <div className="absolute inset-0 opacity-30 dark:opacity-10">
        <div className="absolute top-20 left-10 w-72 h-72 bg-primary-300 rounded-full mix-blend-multiply filter blur-xl animate-blob"></div>
        <div className="absolute top-40 right-10 w-72 h-72 bg-purple-300 rounded-full mix-blend-multiply filter blur-xl animate-blob animation-delay-2000"></div>
        <div className="absolute bottom-20 left-1/2 w-72 h-72 bg-blue-300 rounded-full mix-blend-multiply filter blur-xl animate-blob animation-delay-4000"></div>
      </div>

      {/* Content */}
      <div className="relative z-10 min-h-screen flex items-center justify-center px-4 py-12">
        <div className="max-w-4xl w-full">
          
          {/* Hero Section */}
          <div className="text-center mb-12">
            {/* Icon with Gradient Background */}
            <div className="inline-flex items-center justify-center mb-6">
              <div className="relative">
                <div className="absolute inset-0 bg-gradient-to-r from-primary-600 to-purple-600 rounded-3xl blur-lg opacity-50"></div>
                <div className="relative bg-gradient-to-br from-primary-600 to-purple-600 p-5 rounded-3xl shadow-xl">
                  <Briefcase className="w-16 h-16 text-white" />
                </div>
              </div>
            </div>

            {/* Headline */}
            <h1 className="text-5xl md:text-6xl font-bold text-neutral-900 dark:text-white mb-6 transition-colors duration-200">
              Welcome to Your
              <span className="block mt-2 bg-gradient-to-r from-primary-600 to-purple-600 bg-clip-text text-transparent">
                AI-Powered Interview
              </span>
            </h1>

            {/* Subtext */}
            <p className="text-xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto leading-relaxed transition-colors duration-200">
              Experience a natural, intelligent conversation that evaluates your skills professionally and objectively
            </p>
          </div>

          {/* Feature Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            {/* Feature 1 */}
            <div className="bg-white/80 dark:bg-neutral-800/80 backdrop-blur-sm rounded-2xl p-6 border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
              <div className="bg-gradient-to-br from-blue-500 to-blue-600 p-3 rounded-xl w-fit mb-4">
                <Sparkles className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-lg font-semibold text-neutral-900 dark:text-white mb-2">Natural Flow</h3>
              <p className="text-sm text-neutral-600 dark:text-neutral-400">
                Conversational experience with no time pressure or stress
              </p>
            </div>

            {/* Feature 2 */}
            <div className="bg-white/80 dark:bg-neutral-800/80 backdrop-blur-sm rounded-2xl p-6 border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
              <div className="bg-gradient-to-br from-purple-500 to-purple-600 p-3 rounded-xl w-fit mb-4">
                <Target className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-lg font-semibold text-neutral-900 dark:text-white mb-2">AI Evaluation</h3>
              <p className="text-sm text-neutral-600 dark:text-neutral-400">
                Objective, unbiased assessment powered by advanced AI
              </p>
            </div>

            {/* Feature 3 */}
            <div className="bg-white/80 dark:bg-neutral-800/80 backdrop-blur-sm rounded-2xl p-6 border border-neutral-200/50 dark:border-neutral-700/50 shadow-lg hover:shadow-xl transition-all duration-300 hover:-translate-y-1">
              <div className="bg-gradient-to-br from-indigo-500 to-indigo-600 p-3 rounded-xl w-fit mb-4">
                <TrendingUp className="w-6 h-6 text-white" />
              </div>
              <h3 className="text-lg font-semibold text-neutral-900 dark:text-white mb-2">Detailed Insights</h3>
              <p className="text-sm text-neutral-600 dark:text-neutral-400">
                Comprehensive feedback on strengths and improvement areas
              </p>
            </div>
          </div>

          {/* Main CTA Card */}
          <div className="bg-white/90 dark:bg-neutral-800/90 backdrop-blur-md rounded-3xl p-10 border border-neutral-200/50 dark:border-neutral-700/50 shadow-2xl">
            {/* What to Expect */}
            <div className="mb-8">
              <h2 className="text-2xl font-bold text-neutral-900 dark:text-white mb-6 text-center">
                What to Expect
              </h2>
              <div className="space-y-4">
                <div className="flex items-start space-x-4">
                  <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-primary-500 to-purple-500 rounded-full flex items-center justify-center text-white font-bold text-sm">
                    1
                  </div>
                  <div className="flex-1">
                    <h4 className="font-semibold text-neutral-900 dark:text-white mb-1">Select Your Role</h4>
                    <p className="text-sm text-neutral-600 dark:text-neutral-400">Choose the position you're interviewing for</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-primary-500 to-purple-500 rounded-full flex items-center justify-center text-white font-bold text-sm">
                    2
                  </div>
                  <div className="flex-1">
                    <h4 className="font-semibold text-neutral-900 dark:text-white mb-1">Three-Stage Interview</h4>
                    <p className="text-sm text-neutral-600 dark:text-neutral-400">Screening, technical, and scenario-based questions</p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-primary-500 to-purple-500 rounded-full flex items-center justify-center text-white font-bold text-sm">
                    3
                  </div>
                  <div className="flex-1">
                    <h4 className="font-semibold text-neutral-900 dark:text-white mb-1">Receive Your Evaluation</h4>
                    <p className="text-sm text-neutral-600 dark:text-neutral-400">Get detailed feedback and recommendations</p>
                  </div>
                </div>
              </div>
            </div>

            {/* Primary CTA Button */}
            <button
              onClick={handleGetStarted}
              className="group w-full px-10 py-5 bg-gradient-to-r from-primary-600 to-purple-600 text-white rounded-2xl hover:from-primary-700 hover:to-purple-700 transition-all duration-300 font-bold text-lg shadow-xl hover:shadow-2xl transform hover:-translate-y-0.5 flex items-center justify-center space-x-3"
            >
              <span>Get Started</span>
              <ArrowRight className="w-6 h-6 group-hover:translate-x-1 transition-transform" />
            </button>

            {/* Duration Info */}
            <p className="text-center text-sm text-neutral-500 dark:text-neutral-400 mt-6">
              <CheckCircle2 className="w-4 h-4 inline mr-1" />
              Estimated duration: 20-30 minutes
            </p>
          </div>

          {/* Footer Note */}
          <p className="text-center text-sm text-neutral-500 dark:text-neutral-400 mt-8">
            Demo version for evaluation purposes
          </p>
        </div>
      </div>

      {/* Custom Animation Styles */}
      <style jsx>{`
        @keyframes blob {
          0%, 100% {
            transform: translate(0, 0) scale(1);
          }
          33% {
            transform: translate(30px, -50px) scale(1.1);
          }
          66% {
            transform: translate(-20px, 20px) scale(0.9);
          }
        }
        .animate-blob {
          animation: blob 7s infinite;
        }
        .animation-delay-2000 {
          animation-delay: 2s;
        }
        .animation-delay-4000 {
          animation-delay: 4s;
        }
      `}</style>
    </div>
  );
};

export default HomePage;
