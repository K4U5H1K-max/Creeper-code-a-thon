# orchestrator/orchestrator_agent.py

import json
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

# Updated to supported model - see https://console.groq.com/docs/models
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

SYSTEM_PROMPT = """
You are the Interview Orchestrator Agent responsible for managing a multi-round interview process.

Your job is to analyze the current interview state and decide the next action:

**Decision Rules:**
1. If no rounds completed yet → start with round_1
2. If round_1 completed:
   - If PASSED → proceed to round_2
   - If FAILED → go to results (REJECTED)
3. If round_2 completed:
   - If PASSED → proceed to round_3
   - If FAILED → go to results (REJECTED)
4. If round_3 completed:
   - If PASSED → go to results (SELECTED)
   - If FAILED → go to results (REJECTED)

**You will receive:**
- Role: The position candidate is interviewing for
- Round results: Including pass/fail status, scores, and feedback

**You must respond with ONLY valid JSON:**
{
  "next_action": "round_1" | "round_2" | "round_3" | "results",
  "reasoning": "Brief explanation of your decision"
}
"""

def run_orchestrator(state: dict):
    """Use LLM to intelligently determine the next round based on interview state."""
    
    # Build context for the LLM
    context = f"""
**Current Interview State:**

Role: {state.get('role', 'Not specified')}

**Round 1 (Screening):**
- Completed: {state.get('round1_result') is not None}
- Passed: {state.get('round1_pass', False)}
- Result: {json.dumps(state.get('round1_result', {}), indent=2) if state.get('round1_result') else 'Not completed'}

**Round 2 (Technical):**
- Completed: {state.get('round2_result') is not None}
- Passed: {state.get('round2_pass', False)}
- Result: {json.dumps(state.get('round2_result', {}), indent=2) if state.get('round2_result') else 'Not completed'}

**Round 3 (Problem-Solving):**
- Completed: {state.get('round3_result') is not None}
- Passed: {state.get('round3_pass', False)}
- Result: {json.dumps(state.get('round3_result', {}), indent=2) if state.get('round3_result') else 'Not completed'}

Based on this state, what should be the next action?
"""
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=context)
    ]
    
    try:
        response = llm.invoke(messages)
        decision = json.loads(response.content)
        
        state["next_action"] = decision.get("next_action")
        state["orchestrator_reasoning"] = decision.get("reasoning")
        
        # Set final decision if going to results
        if decision.get("next_action") == "results":
            if state.get("round3_pass"):
                state["decision"] = "SELECTED"
            else:
                state["decision"] = "REJECTED"
        
    except Exception as e:
        # Fallback to rule-based logic if LLM fails
        print(f"LLM decision failed: {e}, using fallback logic")
        
        if state.get('round1_result') is None:
            state["next_action"] = "round_1"
        elif state.get('round1_pass') and state.get('round2_result') is None:
            state["next_action"] = "round_2"
        elif state.get('round2_pass') and state.get('round3_result') is None:
            state["next_action"] = "round_3"
        else:
            state["next_action"] = "results"
            state["decision"] = "SELECTED" if state.get('round3_pass') else "REJECTED"
    
    return state
