# orchestrator/orchestrator_agent.py

from langchain_groq import ChatGroq
from langchain.schema import SystemMessage
from langchain.agents import create_tool_calling_agent, AgentExecutor
from orchestrator.tools import round_1_tool, round_2_tool, round_3_tool

llm = ChatGroq(model="llama-3.1-70b-versatile")

SYSTEM_PROMPT = """
You are the Interview Orchestrator Agent.
You have access to tools that conduct interview rounds.

Rules:
- If no rounds are done yet, call round_1_tool.
- If Round 1 passed, call round_2_tool.
- If Round 2 passed, call round_3_tool.
- If any round fails, stop and mark REJECTED.
- Only SELECTED after Round 3 passes.
Return structured JSON in your final answer:
{
  "next_round": "round_1" | "round_2" | "round_3" | "end",
  "decision": "SELECTED" | "REJECTED" | null
}
"""

tools = [round_1_tool, round_2_tool, round_3_tool]

agent = create_tool_calling_agent(llm, tools, SYSTEM_PROMPT)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def run_orchestrator(state: dict):
    result = executor.invoke({"input": str(state)})
    return result
