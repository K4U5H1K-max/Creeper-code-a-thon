import React from 'react';
import { Check } from 'lucide-react';

/**
 * ProgressStepper Component
 * Visual indicator showing interview rounds and current progress
 * 
 * @param {Array} rounds - Array of round objects with id, name, and description
 * @param {number} currentRound - Current active round number (1-3)
 */
const ProgressStepper = ({ rounds, currentRound }) => {
  return (
    <div className="bg-white dark:bg-neutral-800 rounded-lg shadow-sm p-6 border border-neutral-200 dark:border-neutral-700 transition-colors duration-200">
      {/* Stepper Container */}
      <div className="flex items-center justify-between relative">
        {rounds.map((round, index) => {
          const isActive = round.id === currentRound;
          const isCompleted = round.id < currentRound;
          const isLast = index === rounds.length - 1;

          return (
            <React.Fragment key={round.id}>
              {/* Step Item */}
              <div className="flex flex-col items-center flex-1 relative z-10">
                {/* Circle Indicator */}
                <div className={`
                  w-12 h-12 rounded-full flex items-center justify-center border-2 transition-all duration-300
                  ${isActive 
                    ? 'bg-primary-600 border-primary-600' 
                    : isCompleted 
                    ? 'bg-green-500 border-green-500' 
                    : 'bg-white dark:bg-neutral-700 border-neutral-300 dark:border-neutral-600'
                  }
                `}>
                  {isCompleted ? (
                    <Check className="w-6 h-6 text-white" />
                  ) : (
                    <span className={`text-sm font-semibold ${
                      isActive ? 'text-white' : 'text-neutral-500 dark:text-neutral-400'
                    }`}>
                      {round.id}
                    </span>
                  )}
                </div>

                {/* Round Label */}
                <div className="mt-3 text-center max-w-[120px]">
                  <p className={`text-sm font-semibold ${
                    isActive ? 'text-primary-600' : 'text-neutral-700 dark:text-neutral-200'
                  }`}>
                    {round.name}
                  </p>
                  <p className="text-xs text-neutral-500 dark:text-neutral-400 mt-1">
                    Round {round.id}
                  </p>
                </div>
              </div>

              {/* Connecting Line */}
              {!isLast && (
                <div className={`
                  flex-1 h-0.5 -mx-4 mt-[-60px] transition-all duration-300
                  ${isCompleted ? 'bg-green-500' : 'bg-neutral-300 dark:bg-neutral-600'}
                `} />
              )}
            </React.Fragment>
          );
        })}
      </div>

      {/* Current Round Description */}
      <div className="mt-6 pt-6 border-t border-neutral-200 dark:border-neutral-700">
        <p className="text-xs text-neutral-500 dark:text-neutral-400 uppercase tracking-wide font-medium mb-1">
          Current Round
        </p>
        <p className="text-sm text-neutral-700 dark:text-neutral-200">
          {rounds[currentRound - 1].description}
        </p>
      </div>
    </div>
  );
};

export default ProgressStepper;
