import React from 'react';
import { CheckCircle2, XCircle, TrendingUp, TrendingDown, Award, RefreshCw } from 'lucide-react';

/**
 * FinalEvaluation Component
 * Displays comprehensive interview results after completion
 * 
 * @param {Object} evaluation - Evaluation data object containing all assessment results
 * @param {Function} onRestart - Callback function to restart the interview (for demo)
 */
const FinalEvaluation = ({ evaluation, onRestart }) => {
  const isRecommended = evaluation.verdict === 'Recommended';

  return (
    <div className="max-w-5xl mx-auto space-y-6">
      {/* Header Card */}
      <div className="bg-white dark:bg-neutral-800 rounded-lg shadow-sm border border-neutral-200 dark:border-neutral-700 p-8 transition-colors duration-200">
        <div className="text-center">
          <div className={`inline-flex items-center justify-center w-16 h-16 rounded-full mb-4 ${
            isRecommended ? 'bg-green-100' : 'bg-red-100'
          }`}>
            {isRecommended ? (
              <CheckCircle2 className="w-8 h-8 text-green-600" />
            ) : (
              <XCircle className="w-8 h-8 text-red-600" />
            )}
          </div>
          <h1 className="text-3xl font-bold text-neutral-900 dark:text-neutral-100 mb-2">
            Interview Evaluation Report
          </h1>
          <p className="text-lg text-neutral-600 dark:text-neutral-400">
            {evaluation.overallScore}
          </p>
        </div>
      </div>

      {/* Verdict Card */}
      <div className={`rounded-lg p-6 border-2 ${
        isRecommended 
          ? 'bg-green-50 dark:bg-green-900/20 border-green-200 dark:border-green-800' 
          : 'bg-red-50 dark:bg-red-900/20 border-red-200 dark:border-red-800'
      }`}>
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-sm font-semibold text-neutral-700 dark:text-neutral-200 uppercase tracking-wide mb-1">
              Final Decision
            </h2>
            <p className={`text-2xl font-bold ${
              isRecommended ? 'text-green-700 dark:text-green-400' : 'text-red-700 dark:text-red-400'
            }`}>
              {evaluation.verdict}
            </p>
          </div>
          <Award className={`w-12 h-12 ${
            isRecommended ? 'text-green-600' : 'text-red-600'
          }`} />
        </div>
      </div>

      {/* Round-wise Performance Summary */}
      <div className="bg-white dark:bg-neutral-800 rounded-lg shadow-sm border border-neutral-200 dark:border-neutral-700 p-6 transition-colors duration-200">
        <h2 className="text-xl font-semibold text-neutral-900 dark:text-neutral-100 mb-6">
          Round-wise Performance
        </h2>
        <div className="space-y-4">
          {evaluation.roundSummaries.map((round, index) => (
            <div 
              key={index}
              className="p-4 bg-neutral-50 dark:bg-neutral-700 rounded-lg border border-neutral-200 dark:border-neutral-600"
            >
              <div className="flex items-start space-x-3">
                <div className="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-semibold text-sm">
                  {index + 1}
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold text-neutral-900 dark:text-neutral-100 mb-2">
                    {round.round}
                  </h3>
                  <p className="text-sm text-neutral-700 dark:text-neutral-300 leading-relaxed">
                    {round.summary}
                  </p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Strengths and Areas for Improvement */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Strengths */}
        <div className="bg-white dark:bg-neutral-800 rounded-lg shadow-sm border border-neutral-200 dark:border-neutral-700 p-6 transition-colors duration-200">
          <div className="flex items-center space-x-2 mb-4">
            <TrendingUp className="w-5 h-5 text-green-600" />
            <h2 className="text-lg font-semibold text-neutral-900 dark:text-neutral-100">
              Key Strengths
            </h2>
          </div>
          <ul className="space-y-3">
            {evaluation.strengths.map((strength, index) => (
              <li key={index} className="flex items-start space-x-3">
                <CheckCircle2 className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                <span className="text-sm text-neutral-700 dark:text-neutral-300">{strength}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Areas for Improvement */}
        <div className="bg-white dark:bg-neutral-800 rounded-lg shadow-sm border border-neutral-200 dark:border-neutral-700 p-6 transition-colors duration-200">
          <div className="flex items-center space-x-2 mb-4">
            <TrendingDown className="w-5 h-5 text-orange-600" />
            <h2 className="text-lg font-semibold text-neutral-900 dark:text-neutral-100">
              Areas for Improvement
            </h2>
          </div>
          <ul className="space-y-3">
            {evaluation.improvements.map((improvement, index) => (
              <li key={index} className="flex items-start space-x-3">
                <div className="w-5 h-5 border-2 border-orange-600 rounded-full flex-shrink-0 mt-0.5" />
                <span className="text-sm text-neutral-700 dark:text-neutral-300">{improvement}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="bg-white dark:bg-neutral-800 rounded-lg shadow-sm border border-neutral-200 dark:border-neutral-700 p-6 transition-colors duration-200">
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button
            onClick={onRestart}
            className="px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors font-medium flex items-center justify-center space-x-2"
          >
            <RefreshCw className="w-5 h-5" />
            <span>Start New Interview</span>
          </button>
          <button className="px-6 py-3 bg-white dark:bg-neutral-700 text-neutral-700 dark:text-neutral-200 border-2 border-neutral-300 dark:border-neutral-600 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-600 transition-colors font-medium">
            Download Report
          </button>
          <button className="px-6 py-3 bg-white dark:bg-neutral-700 text-neutral-700 dark:text-neutral-200 border-2 border-neutral-300 dark:border-neutral-600 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-600 transition-colors font-medium">
            Share Feedback
          </button>
        </div>
      </div>

      {/* Footer Note */}
      <div className="text-center">
        <p className="text-sm text-neutral-500 dark:text-neutral-400">
          Generated on {new Date().toLocaleDateString('en-US', { 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
          })}
        </p>
      </div>
    </div>
  );
};

export default FinalEvaluation;
