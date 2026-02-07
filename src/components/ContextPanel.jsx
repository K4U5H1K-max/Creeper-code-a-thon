import React from 'react';
import { Info, Clock } from 'lucide-react';

/**
 * ContextPanel Component
 * Displays current round information and context
 * 
 * @param {Object} currentRound - Current round object with name and description
 */
const ContextPanel = ({ currentRound }) => {
  return (
    <div className="bg-white dark:bg-neutral-800 rounded-lg shadow-sm border border-neutral-200 dark:border-neutral-700 p-6 transition-colors duration-200">
      {/* Panel Header */}
      <div className="flex items-center space-x-2 mb-4">
        <Info className="w-5 h-5 text-primary-600" />
        <h3 className="text-lg font-semibold text-neutral-900 dark:text-neutral-100">
          Round Information
        </h3>
      </div>

      {/* Current Round Details */}
      <div className="space-y-4">
        {/* Round Name Badge */}
        <div>
          <span className="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-primary-100 text-primary-700">
            Round {currentRound.id}: {currentRound.name}
          </span>
        </div>

        {/* Round Description */}
        <div>
          <h4 className="text-sm font-semibold text-neutral-700 dark:text-neutral-200 mb-2">
            Focus Area
          </h4>
          <p className="text-sm text-neutral-600 dark:text-neutral-400 leading-relaxed">
            {currentRound.description}
          </p>
        </div>

        {/* Guidelines */}
        <div className="pt-4 border-t border-neutral-200 dark:border-neutral-700">
          <h4 className="text-sm font-semibold text-neutral-700 dark:text-neutral-200 mb-3">
            Interview Tips
          </h4>
          <ul className="space-y-2 text-sm text-neutral-600 dark:text-neutral-400">
            <li className="flex items-start">
              <span className="w-1.5 h-1.5 bg-primary-600 rounded-full mt-1.5 mr-2 flex-shrink-0" />
              <span>Take your time to think before responding</span>
            </li>
            <li className="flex items-start">
              <span className="w-1.5 h-1.5 bg-primary-600 rounded-full mt-1.5 mr-2 flex-shrink-0" />
              <span>Be specific and provide examples when possible</span>
            </li>
            <li className="flex items-start">
              <span className="w-1.5 h-1.5 bg-primary-600 rounded-full mt-1.5 mr-2 flex-shrink-0" />
              <span>Ask for clarification if needed</span>
            </li>
          </ul>
        </div>

        {/* Status Indicator */}
        <div className="pt-4 border-t border-neutral-200 dark:border-neutral-700">
          <div className="flex items-center space-x-2 text-sm">
            <Clock className="w-4 h-4 text-neutral-500 dark:text-neutral-400" />
            <span className="text-neutral-600 dark:text-neutral-400">No time limit - answer thoughtfully</span>
          </div>
        </div>
      </div>

      {/* Additional Context (Optional) */}
      <div className="mt-6 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-100 dark:border-blue-800">
        <p className="text-xs text-blue-800 dark:text-blue-300 leading-relaxed">
          <span className="font-semibold">Note:</span> Your responses are being evaluated in real-time. The AI interviewer will adjust questions based on your answers.
        </p>
      </div>
    </div>
  );
};

export default ContextPanel;
