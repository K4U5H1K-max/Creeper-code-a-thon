# orchestrator/state.py

from typing import TypedDict, Optional, List, Dict, Any

class InterviewState(TypedDict, total=False):
    role: Optional[str]
    round1_result: Optional[Dict[str, Any]]
    round2_result: Optional[Dict[str, Any]]
    round3_result: Optional[Dict[str, Any]]
    round1_pass: bool
    round2_pass: bool
    round3_pass: bool
    next_action: Optional[str]
    decision: Optional[str]
    orchestrator_reasoning: Optional[str]
    round1_state: Dict[str, Any]
    round2_state: Dict[str, Any]
    round3_state: Dict[str, Any]
    final_results: Optional[Dict[str, Any]]

def init_state() -> InterviewState:
    return {
        "role": None,
        "round1_result": None,
        "round2_result": None,
        "round3_result": None,
        "round1_pass": False,
        "round2_pass": False,
        "round3_pass": False,
        "next_action": "collect_role",
        "decision": None,
        "orchestrator_reasoning": None,
        "round1_state": {"history": [], "question_count": 0},
        "round2_state": {"history": [], "question_count": 0},
        "round3_state": {"history": [], "question_count": 0},
        "final_results": None
    }
