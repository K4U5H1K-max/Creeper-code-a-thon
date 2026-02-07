import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useInterview } from '../context/InterviewContext';
import Header from '../components/Header';
import FinalEvaluation from '../components/FinalEvaluation';

/**
 * EvaluationPage Component
 * Displays the final interview evaluation and results
 * Only accessible after completing all rounds or failing a round
 */
const EvaluationPage = () => {
  const navigate = useNavigate();
  const { sessionId, finalEvaluation, roundPassed, resetInterview } = useInterview();

  // Redirect if no session
  useEffect(() => {
    if (!sessionId) {
      navigate('/job-selection');
    }
  }, [sessionId, navigate]);

  // Convert backend evaluation to frontend format
  const getEvaluationData = () => {
    if (finalEvaluation) {
      const roundNames = ['Screening', 'Technical', 'Scenario'];
      
      return {
        roundSummaries: Object.entries(finalEvaluation.round_breakdown || {}).map(([roundNum, score]) => ({
          round: `Round ${roundNum}: ${roundNames[parseInt(roundNum) - 1]}`,
          summary: `Score: ${score.toFixed(1)}% - ${getScoreDescription(score)}`
        })),
        batch: finalEvaluation.batch,
        overallScore: finalEvaluation.overall_score,
        confidenceScore: finalEvaluation.confidence_score,
        recommendation: finalEvaluation.recommendation,
        summary: finalEvaluation.summary,
        strengths: getStrengthsFromScore(finalEvaluation.overall_score),
        improvements: getImprovementsFromScore(finalEvaluation.overall_score),
        verdict: finalEvaluation.recommendation
      };
    }
    
    // If no final evaluation (failed a round)
    if (roundPassed === false) {
      return {
        roundSummaries: [],
        verdict: 'Not Recommended',
        overallScore: 'Unfortunately, the requirements for this round were not met. We encourage you to continue developing your skills.',
        strengths: [],
        improvements: ['Review the feedback provided', 'Practice interview skills', 'Strengthen core competencies']
      };
    }

    return null;
  };

  const getScoreDescription = (score) => {
    if (score >= 85) return 'Excellent performance';
    if (score >= 75) return 'Strong performance';
    if (score >= 65) return 'Good performance';
    if (score >= 60) return 'Satisfactory performance';
    return 'Needs improvement';
  };

  const getStrengthsFromScore = (score) => {
    const strengths = [];
    if (score >= 80) {
      strengths.push('Excellent overall performance across all rounds');
      strengths.push('Strong technical and problem-solving skills');
    } else if (score >= 70) {
      strengths.push('Good performance in most areas');
      strengths.push('Demonstrates core competencies');
    } else if (score >= 60) {
      strengths.push('Meets basic requirements');
      strengths.push('Shows potential for growth');
    }
    return strengths;
  };

  const getImprovementsFromScore = (score) => {
    const improvements = [];
    if (score < 80) {
      improvements.push ('Strengthen technical depth');
      improvements.push('Practice problem-solving scenarios');
    }
    if (score < 70) {
      improvements.push('Improve communication clarity');
      improvements.push('Develop more structured approaches');
    }
    return improvements;
  };

  const handleRestart = () => {
    resetInterview();
    navigate('/');
  };

  const evaluationData = getEvaluationData();

  if (!evaluationData) {
    return null;
  }

  return (
    <div className="min-h-screen bg-neutral-50 dark:bg-neutral-900 transition-colors duration-200">
      {/* Header */}
      <Header status="Interview Completed" />

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <FinalEvaluation 
          evaluation={evaluationData}
          onRestart={handleRestart}
        />
      </div>
    </div>
  );
};

export default EvaluationPage;
