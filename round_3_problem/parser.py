# parser.py
import json

def parse_output(response_text: str):
    try:
        return json.loads(response_text)
    except Exception as e:
        return {
            "next_action": "final_decision",
            "question": None,
            "scores": {},
            "pass": False,
            "short_feedback": "Invalid JSON from LLM.",
            "confidence": 0.0,
            "error": str(e)
        }
