"""
Data models for the interview system.
"""

from typing import List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class Message(BaseModel):
    """Represents a single message in the conversation."""
    role: str  # 'user', 'assistant', or 'system'
    content: str
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())

class QuestionAnswer(BaseModel):
    """Represents a question-answer pair."""
    question_number: int
    question: str
    answer: str
    ai_feedback: str
    score: float = 0.0

class RoundData(BaseModel):
    """Represents data for a single interview round."""
    round_number: int
    round_name: str
    status: str = "not_started"  # not_started, in_progress, completed, failed
    questions: List[QuestionAnswer] = []
    round_score: float = 0.0
    passed: bool = False
    feedback: str = ""

class InterviewSession(BaseModel):
    """Represents a complete interview session."""
    session_id: str
    job_role: str
    candidate_name: Optional[str] = None
    current_round: int = 1
    current_question: int = 0
    status: str = "active"  # active, completed, terminated
    rounds: Dict[int, RoundData] = {}
    conversation_history: List[Message] = []
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    completed_at: Optional[str] = None
    final_evaluation: Optional[Dict] = None

class StartInterviewRequest(BaseModel):
    """Request to start a new interview."""
    job_role: str
    candidate_name: Optional[str] = None

class ChatRequest(BaseModel):
    """Request to send a message in the interview."""
    session_id: str
    message: str

class ChatResponse(BaseModel):
    """Response from the AI interviewer."""
    session_id: str
    ai_message: str
    current_round: int
    current_question: int
    total_questions: int
    round_complete: bool = False
    round_passed: Optional[bool] = None
    interview_complete: bool = False
    round_feedback: Optional[str] = None
    final_evaluation: Optional[Dict] = None
