# backend/gpt_response.py
from memory_manager import query_memories
import requests
import os

# Use LM Studio / DeepSeek / Local model URL
LLM_API_URL = os.getenv("LLM_API_URL", "http://localhost:1234/v1/chat/completions")

def generate_reply_with_memory(query: str):
    top_memories = query_memories(query)
    memory_context = "\n".join(f"- {m['content']}" for m in top_memories)

    prompt = f"""You are an AI clone that talks like the user. 
Below are your past memories:
{memory_context}

Answer the following based on the above:
Q: {query}
A:"""

    payload = {
        "model": "gpt-4",  # or your local model name
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    res = requests.post(LLM_API_URL, json=payload)
    return res.json()["choices"][0]["message"]["content"]
