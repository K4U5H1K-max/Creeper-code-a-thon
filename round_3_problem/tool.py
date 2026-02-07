# tool.py

import os
from groq import Groq
from prompts.prompts import ROUND_3_APTITUDE_SYSTEM_PROMPT
from .parser import parse_output

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Best model choices:
# "llama-3.1-70b-versatile" -> best reasoning
# "llama-3.1-8b-instant"   -> fastest (recommended for hackathon)
MODEL_NAME = "llama-3.1-70b-versatile"

def run_round3(state):
    messages = [
        {"role": "system", "content": ROUND_3_APTITUDE_SYSTEM_PROMPT},
        *state["history"]
    ]

    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.3,
        max_tokens=512,
    )

    response_text = resp.choices[0].message.content
    return parse_output(response_text)


def update_state_with_interaction(state, question, answer):
    state["history"].append({"role": "assistant", "content": question})
    state["history"].append({"role": "user", "content": answer})
    state["question_count"] += 1
