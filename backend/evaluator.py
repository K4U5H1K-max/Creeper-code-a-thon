"""
Evaluation logic for assessing candidate performance and determining pass/fail.
"""

from typing import Dict, List, Tuple
import re

class InterviewEvaluator:
    """Handles evaluation of candidate responses and overall performance."""
    
    # Passing thresholds for each round (out of 100)
    ROUND_THRESHOLDS = {
        1: 60,  # Screening: 60% to pass
        2: 65,  # Technical: 65% to pass
        3: 70   # Scenario: 70% to pass
    }
    
    # Batch assignment based on overall score
    BATCH_CRITERIA = {
        'A+': (90, 100),
        'A': (80, 89),
        'B+': (70, 79),
        'B': (60, 69),
        'C': (50, 59),
        'D': (0, 49)
    }
    
    @staticmethod
    def evaluate_response_quality(response: str) -> Dict[str, float]:
        """
        Evaluate the quality of a single response.
        Returns scores for different criteria.
        """
        scores = {
            'length_score': 0.0,
            'coherence_score': 0.0,
            'relevance_score': 0.0
        }
        
        # Length score (penalize too short or too long)
        word_count = len(response.split())
        if word_count < 10:
            scores['length_score'] = min(word_count * 3, 30)
        elif word_count > 300:
            scores['length_score'] = max(100 - (word_count - 300) * 0.2, 70)
        else:
            scores['length_score'] = min(70 + (word_count - 10) * 0.1, 100)
        
        # Coherence score (basic sentence structure check)
        sentences = response.count('.') + response.count('!') + response.count('?')
        if sentences > 0 and word_count > 0:
            avg_sentence_length = word_count / sentences
            if 5 <= avg_sentence_length <= 25:
                scores['coherence_score'] = 85
            else:
                scores['coherence_score'] = 60
        else:
            scores['coherence_score'] = 40
        
        # Relevance score (check for technical terms, proper nouns, etc.)
        has_capitals = bool(re.search(r'[A-Z][a-z]+', response))
        has_technical_indicators = any(indicator in response.lower() for indicator in 
                                      ['experience', 'project', 'develop', 'implement', 
                                       'manage', 'design', 'build', 'create', 'solve'])
        
        if has_capitals and has_technical_indicators:
            scores['relevance_score'] = 85
        elif has_capitals or has_technical_indicators:
            scores['relevance_score'] = 70
        else:
            scores['relevance_score'] = 55
        
        return scores
    
    @staticmethod
    def extract_ai_evaluation(ai_response: str) -> float:
        """
        Extract evaluation signals from AI's response to candidate.
        Returns a score based on AI's feedback tone.
        """
        ai_lower = ai_response.lower()
        
        # Positive indicators
        positive_words = ['excellent', 'great', 'good', 'well', 'correct', 
                         'strong', 'impressive', 'solid', 'perfect', 'clear']
        positive_count = sum(1 for word in positive_words if word in ai_lower)
        
        # Negative indicators
        negative_words = ['however', 'but', 'unfortunately', 'incorrect', 
                         'missing', 'unclear', 'weak', 'limited', 'lacking']
        negative_count = sum(1 for word in negative_words if word in ai_lower)
        
        # Calculate base score
        if positive_count > negative_count:
            base_score = 75 + min(positive_count * 5, 25)
        elif negative_count > positive_count:
            base_score = 50 - min(negative_count * 5, 30)
        else:
            base_score = 65
        
        return max(0, min(100, base_score))
    
    @staticmethod
    def calculate_question_score(response: str, ai_feedback: str, question_number: int, 
                                 total_questions: int) -> float:
        """
        Calculate score for a single question-answer pair.
        """
        quality_scores = InterviewEvaluator.evaluate_response_quality(response)
        ai_score = InterviewEvaluator.extract_ai_evaluation(ai_feedback)
        
        # Weighted combination
        quality_weight = 0.3
        ai_weight = 0.7
        
        question_score = (
            quality_scores['length_score'] * 0.1 * quality_weight +
            quality_scores['coherence_score'] * 0.3 * quality_weight +
            quality_scores['relevance_score'] * 0.6 * quality_weight +
            ai_score * ai_weight
        )
        
        # Later questions in technical rounds might be harder, slightly boost earlier ones
        if question_number <= total_questions // 2:
            question_score *= 1.05
        
        return min(100, question_score)
    
    @staticmethod
    def calculate_round_score(question_scores: List[float], round_number: int) -> float:
        """
        Calculate overall score for a round based on all question scores.
        """
        if not question_scores:
            return 0.0
        
        # Weight distribution based on round type
        if round_number == 2:  # Technical round - later questions worth more
            weights = [0.15, 0.18, 0.20, 0.22, 0.25][:len(question_scores)]
        elif round_number == 3:  # Scenario round - all questions equally important
            weights = [1/len(question_scores)] * len(question_scores)
        else:  # Screening round - equal weights
            weights = [1/len(question_scores)] * len(question_scores)
        
        # Normalize weights
        total_weight = sum(weights)
        weights = [w / total_weight for w in weights]
        
        # Calculate weighted average
        round_score = sum(score * weight for score, weight in zip(question_scores, weights))
        
        return round(round_score, 2)
    
    @staticmethod
    def determine_round_pass(round_score: float, round_number: int) -> Tuple[bool, str]:
        """
        Determine if candidate passed the round.
        Returns (passed: bool, feedback: str)
        """
        threshold = InterviewEvaluator.ROUND_THRESHOLDS.get(round_number, 65)
        passed = round_score >= threshold
        
        if passed:
            if round_score >= 85:
                feedback = f"Outstanding performance! Score: {round_score:.1f}%. You've demonstrated excellent skills."
            elif round_score >= 75:
                feedback = f"Strong performance! Score: {round_score:.1f}%. You're well-prepared for the next round."
            else:
                feedback = f"Good performance. Score: {round_score:.1f}%. You've met the requirements to proceed."
        else:
            feedback = f"Score: {round_score:.1f}%. Unfortunately, this doesn't meet our threshold of {threshold}% for this round."
        
        return passed, feedback
    
    @staticmethod
    def calculate_final_evaluation(round_scores: Dict[int, float]) -> Dict:
        """
        Calculate final evaluation with overall score, batch, and confidence.
        """
        # Weight each round differently
        round_weights = {
            1: 0.20,  # Screening: 20%
            2: 0.45,  # Technical: 45%
            3: 0.35   # Scenario: 35%
        }
        
        # Calculate weighted overall score
        overall_score = sum(
            round_scores.get(round_num, 0) * weight 
            for round_num, weight in round_weights.items()
        )
        
        # Determine batch
        batch = 'D'
        for batch_name, (min_score, max_score) in InterviewEvaluator.BATCH_CRITERIA.items():
            if min_score <= overall_score <= max_score:
                batch = batch_name
                break
        
        # Calculate confidence score (how consistent were the performances)
        scores_list = list(round_scores.values())
        if len(scores_list) > 1:
            score_variance = sum((s - overall_score) ** 2 for s in scores_list) / len(scores_list)
            consistency_factor = max(0, 100 - score_variance / 2)
            confidence = (overall_score + consistency_factor) / 2
        else:
            confidence = overall_score
        
        # Determine recommendation
        if overall_score >= 80:
            recommendation = "STRONG HIRE"
            summary = "Candidate demonstrated excellent performance across all rounds. Highly recommended for the position."
        elif overall_score >= 70:
            recommendation = "HIRE"
            summary = "Candidate showed good competency and fits the role requirements. Recommended for hire."
        elif overall_score >= 60:
            recommendation = "CONSIDER"
            summary = "Candidate has potential but showed some gaps. Consider for junior positions or with additional training."
        else:
            recommendation = "NO HIRE"
            summary = "Candidate did not meet the minimum requirements for the position."
        
        return {
            'overall_score': round(overall_score, 2),
            'confidence_score': round(confidence, 2),
            'batch': batch,
            'recommendation': recommendation,
            'summary': summary,
            'round_breakdown': round_scores
        }
