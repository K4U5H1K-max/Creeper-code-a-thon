# tool.py

from prompts.prompts import ROUND_1
from .parser import parse_output

def run_round1(state, llm):
    """
    Runs Round 1 screening interview.
    state: dict from init_round1_state()
    llm: any LangChain / OpenAI / custom LLM wrapper with invoke()
    """

    messages = [
        {"role": "system", "content": ROUND_1},
        *state["history"]
    ]

    # Call LLM
    response = llm.invoke(messages)

    # Parse JSON safely
    result = parse_output(response)

    return result


def update_state_with_interaction(state, question, answer):
    """Stores conversation history."""
    state["history"].append({"role": "assistant", "content": question})
    state["history"].append({"role": "user", "content": answer})
    state["question_count"] += 1
