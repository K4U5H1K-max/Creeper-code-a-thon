# orchestrator/graph.py

from langgraph.graph import StateGraph, END
from orchestrator.orchestrator_agent import run_orchestrator
from orchestrator.state import init_state, InterviewState
from round_1_screening.tool import run_round1
from round_2_technical.tool import run_round2
from round_3_problem.tool import run_round3
from langchain_groq import ChatGroq

# Updated to supported model - see https://console.groq.com/docs/models
llm = ChatGroq(model="llama-3.3-70b-versatile")

def collect_role_node(state):
    """Collect the role the candidate is interviewing for."""
    if state.get("role") is None:
        # In a real scenario, this would be user input
        # For now, we'll set a placeholder
        return {"role": "Software Engineer"}
    return {}

def orchestrator_node(state):
    """Central orchestrator that uses LLM to decide next action based on round results."""
    # Create a copy to avoid modifying input
    state_copy = state.copy()
    result = run_orchestrator(state_copy)
    
    # Return only the fields that changed
    return {
        "next_action": result.get("next_action"),
        "orchestrator_reasoning": result.get("orchestrator_reasoning"),
        "decision": result.get("decision")
    }

def round_1_node(state):
    """Run Round 1 screening interview."""
    role = state["role"]
    round_state = state.get("round1_state", {"history": [], "question_count": 0}).copy()
    
    # Add role context to the first message if history is empty
    if not round_state["history"]:
        round_state["history"] = round_state.get("history", []).copy()
        round_state["history"].append({
            "role": "user", 
            "content": f"I am interviewing for the role: {role}"
        })
    
    result = run_round1(round_state, llm)
    
    return {
        "round1_result": result,
        "round1_pass": result.get("pass", False),
        "round1_state": round_state
    }

def round_2_node(state):
    """Run Round 2 technical interview."""
    role = state["role"]
    round_state = state.get("round2_state", {"history": [], "question_count": 0}).copy()
    
    # Add role context
    if not round_state["history"]:
        round_state["history"] = round_state.get("history", []).copy()
        round_state["history"].append({
            "role": "user",
            "content": f"I am interviewing for the role: {role}"
        })
    
    result = run_round2(round_state, llm)
    
    return {
        "round2_result": result,
        "round2_pass": result.get("pass", False),
        "round2_state": round_state
    }

def round_3_node(state):
    """Run Round 3 problem-solving interview."""
    role = state["role"]
    round_state = state.get("round3_state", {"history": [], "question_count": 0}).copy()
    
    # Add role context
    if not round_state["history"]:
        round_state["history"] = round_state.get("history", []).copy()
        round_state["history"].append({
            "role": "user",
            "content": f"I am interviewing for the role: {role}"
        })
    
    result = run_round3(round_state)
    
    return {
        "round3_result": result,
        "round3_pass": result.get("pass", False),
        "round3_state": round_state
    }

def results_node(state):
    """Display final results with scores and feedback."""
    decision = state.get("decision", "UNKNOWN")
    role = state.get("role", "Unknown Role")
    
    # Compile results
    results_summary = {
        "role": role,
        "final_decision": decision,
        "rounds_summary": []
    }
    
    # Round 1 summary
    if state.get("round1_result"):
        r1 = state["round1_result"]
        results_summary["rounds_summary"].append({
            "round": "Round 1 - Screening",
            "passed": state.get("round1_pass", False),
            "scores": r1.get("scores", {}),
            "feedback": r1.get("short_feedback", "No feedback available"),
            "confidence": r1.get("confidence", 0)
        })
    
    # Round 2 summary
    if state.get("round2_result"):
        r2 = state["round2_result"]
        results_summary["rounds_summary"].append({
            "round": "Round 2 - Technical",
            "passed": state.get("round2_pass", False),
            "scores": r2.get("scores", {}),
            "feedback": r2.get("short_feedback", "No feedback available"),
            "confidence": r2.get("confidence", 0)
        })
    
    # Round 3 summary
    if state.get("round3_result"):
        r3 = state["round3_result"]
        results_summary["rounds_summary"].append({
            "round": "Round 3 - Problem Solving",
            "passed": state.get("round3_pass", False),
            "scores": r3.get("scores", {}),
            "feedback": r3.get("short_feedback", "No feedback available"),
            "confidence": r3.get("confidence", 0)
        })
    
    # Add overall reason
    if decision == "SELECTED":
        results_summary["reason"] = "Candidate successfully passed all interview rounds and demonstrated strong competencies."
    else:
        failed_rounds = [r["round"] for r in results_summary["rounds_summary"] if not r["passed"]]
        if failed_rounds:
            results_summary["reason"] = f"Candidate did not meet the requirements. Failed: {', '.join(failed_rounds)}"
        else:
            results_summary["reason"] = "Candidate did not complete all required rounds."
    
    print("\n" + "="*60)
    print(f"FINAL INTERVIEW RESULTS - {role}")
    print("="*60)
    print(f"Decision: {decision}")
    print(f"\nReason: {results_summary['reason']}")
    print("\nRound-by-Round Breakdown:")
    for round_info in results_summary["rounds_summary"]:
        print(f"\n{round_info['round']}:")
        print(f"  Status: {'✓ PASSED' if round_info['passed'] else '✗ FAILED'}")
        print(f"  Scores: {round_info['scores']}")
        print(f"  Feedback: {round_info['feedback']}")
        print(f"  Confidence: {round_info['confidence']:.2f}")
    print("="*60 + "\n")
    
    return {"final_results": results_summary}

def route_orchestrator(state):
    """Route based on orchestrator's decision."""
    return state.get("next_action", "results")

def build_graph():
    g = StateGraph(InterviewState)
    
    # Add all nodes
    g.add_node("collect_role", collect_role_node)
    g.add_node("orchestrator", orchestrator_node)
    g.add_node("round_1", round_1_node)
    g.add_node("round_2", round_2_node)
    g.add_node("round_3", round_3_node)
    g.add_node("results", results_node)
    
    # Set entry point
    g.set_entry_point("collect_role")
    
    # collect_role always goes to orchestrator
    g.add_edge("collect_role", "orchestrator")
    
    # Orchestrator routes to rounds or results
    g.add_conditional_edges(
        "orchestrator",
        route_orchestrator,
        {
            "round_1": "round_1",
            "round_2": "round_2",
            "round_3": "round_3",
            "results": "results"
        }
    )
    
    # All rounds go back to orchestrator for decision
    g.add_edge("round_1", "orchestrator")
    g.add_edge("round_2", "orchestrator")
    g.add_edge("round_3", "orchestrator")
    
    # Results is the final node
    g.add_edge("results", END)
    
    return g.compile()
