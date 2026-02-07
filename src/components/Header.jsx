import React from 'react';
import { Briefcase, Sun, Moon } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';

/**
 * Header Component
 * Displays the application name, current interview status, and theme toggle
 * 
 * @param {string} status - Current interview status ("Interview In Progress" or "Interview Completed")
 */
const Header = ({ status }) => {
  const { theme, toggleTheme, isDark } = useTheme();

  return (
    <header className="bg-white dark:bg-neutral-900 border-b border-neutral-200 dark:border-neutral-700 shadow-sm transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* App Logo and Name */}
          <div className="flex items-center space-x-3">
            <div className="bg-primary-600 dark:bg-primary-500 p-2 rounded-lg transition-colors duration-200">
              <Briefcase className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-semibold text-neutral-900 dark:text-neutral-100 transition-colors duration-200">
                AI Interview Platform
              </h1>
            </div>
          </div>

          {/* Status and Theme Toggle */}
          <div className="flex items-center space-x-4">
            {/* Interview Status */}
            <div className="flex items-center space-x-2">
              <div className={`w-2 h-2 rounded-full ${
                status === 'Interview Completed' ? 'bg-green-500' : 'bg-blue-500 animate-pulse'
              }`} />
              <span className="text-sm font-medium text-neutral-600 dark:text-neutral-400 transition-colors duration-200">
                {status}
              </span>
            </div>

            {/* Theme Toggle Button */}
            <button
              onClick={toggleTheme}
              className="p-2 rounded-lg bg-neutral-100 dark:bg-neutral-800 hover:bg-neutral-200 dark:hover:bg-neutral-700 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2 dark:focus:ring-offset-neutral-900"
              aria-label="Toggle theme"
              title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
            >
              {isDark ? (
                <Sun className="w-5 h-5 text-amber-500" />
              ) : (
                <Moon className="w-5 h-5 text-neutral-600" />
              )}
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
