from memory_manager import query_memories
import subprocess

def format_prompt(query, top_memories):
    prompt = "You are an AI clone of the user. Respond naturally based on these memories:\n\n"
    for i, m in enumerate(top_memories):
        prompt += f"{i+1}. {str(m['text'])}\n"  # Ensure it's always a string
    prompt += f"\nNow answer this: {query}\n"
    return prompt

def generate_reply_with_memory(query):
    top_memories = query_memories(query)

    # Build prompt from text only
    prompt = "You are an AI clone of the user. Respond naturally based on these memories:\n\n"
    for i, m in enumerate(top_memories):
        prompt += f"{i+1}. {m['text']}\n"
    prompt += f"\nNow answer this: {query}\n"

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True
    )

    response = result.stdout.decode().strip()

    # ✅ Strip out embeddings, return only text memories
    memory_texts = [m["text"] for m in top_memories]

    return {
        "reply": response,
        "memories_used": memory_texts
    }

