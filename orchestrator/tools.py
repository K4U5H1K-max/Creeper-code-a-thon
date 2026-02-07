# orchestrator/tools.py

from langchain.tools import tool
from rounds.round_1_screening.tool import run_round1
from rounds.round_2_technical.tool import run_round2
from rounds.round_3_aptitude.tool import run_round3

@tool
def round_1_tool(state_json: str) -> str:
    """Run Round 1 screening interview and return JSON result."""
    return str(run_round1(eval(state_json)))

@tool
def round_2_tool(state_json: str) -> str:
    """Run Round 2 technical interview and return JSON result."""
    return str(run_round2(eval(state_json)))

@tool
def round_3_tool(state_json: str) -> str:
    """Run Round 3 aptitude/problem-solving interview and return JSON result."""
    return str(run_round3(eval(state_json)))
