/**
 * API Service for Multi-Round Interview Backend
 * Handles all communication with the Flask backend
 */

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000/api';

/**
 * Interview API Service
 * All methods for interacting with the interview backend
 */
export const interviewAPI = {
  /**
   * Start a new interview session
   * @param {string} jobRole - The job role for the interview
   * @param {string|null} candidateName - Optional candidate name
   * @returns {Promise<Object>} - Session data with greeting
   */
  async startInterview(jobRole, candidateName = null) {
    try {
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
        const error = await response.json();
        throw new Error(error.error || 'Failed to start interview');
      }

      return await response.json();
    } catch (error) {
      console.error('Error starting interview:', error);
      throw error;
    }
  },

  /**
   * Send a chat message during the interview
   * @param {string} sessionId - Current session ID
   * @param {string} message - User's message
   * @returns {Promise<Object>} - AI response and session status
   */
  async sendMessage(sessionId, message) {
    try {
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
        const error = await response.json();
        throw new Error(error.error || 'Failed to send message');
      }

      return await response.json();
    } catch (error) {
      console.error('Error sending message:', error);
      throw error;
    }
  },

  /**
   * Get current session status
   * @param {string} sessionId - Session ID to query
   * @returns {Promise<Object>} - Complete session data
   */
  async getSession(sessionId) {
    try {
      const response = await fetch(`${API_BASE_URL}/session/${sessionId}`);

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Failed to get session');
      }

      return await response.json();
    } catch (error) {
      console.error('Error getting session:', error);
      throw error;
    }
  },

  /**
   * Get conversation history for a session
   * @param {string} sessionId - Session ID to query
   * @returns {Promise<Object>} - Conversation history
   */
  async getHistory(sessionId) {
    try {
      const response = await fetch(`${API_BASE_URL}/session/${sessionId}/history`);

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Failed to get history');
      }

      return await response.json();
    } catch (error) {
      console.error('Error getting history:', error);
      throw error;
    }
  },

  /**
   * Health check endpoint
   * @returns {Promise<Object>} - Health status
   */
  async healthCheck() {
    try {
      const response = await fetch('http://localhost:5000/health');
      
      if (!response.ok) {
        throw new Error('Backend is not healthy');
      }

      return await response.json();
    } catch (error) {
      console.error('Health check failed:', error);
      throw error;
    }
  }
};

export default interviewAPI;
