# orchestrator/graph.py

from langgraph.graph import StateGraph, END
from orchestrator.orchestrator_agent import run_orchestrator
from orchestrator.state import init_state

def orchestrator_node(state):
    agent_result = run_orchestrator(state)
    # Agent result should contain next_round + decision
    state.update(agent_result.get("output", {}))
    return state

def route_from_orchestrator(state):
    return state["next_round"]

def build_graph():
    g = StateGraph(dict)
    g.add_node("orchestrator", orchestrator_node)
    g.set_entry_point("orchestrator")

    g.add_conditional_edges(
        "orchestrator",
        route_from_orchestrator,
        {
            "round_1": "orchestrator",
            "round_2": "orchestrator",
            "round_3": "orchestrator",
            "end": END
        }
    )
    return g.compile()
