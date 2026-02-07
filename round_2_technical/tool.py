# tool.py

from prompts.prompts import ROUND_2_TECHNICAL_SYSTEM_PROMPT
from .parser import parse_output

def run_round2(state, llm):
    messages = [
        {"role": "system", "content": ROUND_2_TECHNICAL_SYSTEM_PROMPT},
        *state["history"]
    ]

    response = llm.invoke(messages)
    response_text = response.content if hasattr(response, "content") else response

    return parse_output(response_text)


def update_state_with_interaction(state, question, answer):
    state["history"].append({"role": "assistant", "content": question})
    state["history"].append({"role": "user", "content": answer})
    state["question_count"] += 1
