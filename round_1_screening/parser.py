# parser.py
import json

def parse_output(response_text: str):
    """
    Ensures LLM returns valid JSON.
    Prevents hackathon demo crashes.
    """
    try:
        return json.loads(response_text)
    except Exception as e:
        return {
            "next_action": "final_decision",
            "question": None,
            "scores": {},
            "pass": False,
            "short_feedback": "LLM returned invalid JSON.",
            "confidence": 0.0,
            "error": str(e)
        }
