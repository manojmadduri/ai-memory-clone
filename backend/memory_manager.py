# backend/memory_manager.py
from sentence_transformers import SentenceTransformer, util
from datetime import datetime, timedelta
from sqlite_client import insert_memory, fetch_all_memories
import ast
import torch

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")  # 384-dim

def embed_text(text: str):
    return model.encode(text).tolist()

def store_memory(text: str, tags=[], image_id=None):
    embedding = embed_text(text)
    insert_memory(text, embedding, tags, image_id)

def get_time_range(time_str):
    now = datetime.now()
    if time_str == "yesterday":
        start = now - timedelta(days=1)
        end = start + timedelta(days=1)
    elif time_str == "last week":
        start = now - timedelta(days=7)
        end = now
    else:
        return None, None
    return start.isoformat(), end.isoformat()

def query_memories(query, time_filter=None):
    query_vec = model.encode(query, convert_to_tensor=True)

    all_memories = fetch_all_memories()
    scored = []
    for m in all_memories:
        if "embedding" not in m or not m["embedding"]:
            continue

        embedding = ast.literal_eval(m["embedding"]) if isinstance(m["embedding"], str) else m["embedding"]
        sim = util.cos_sim(query_vec, torch.tensor(embedding))[0][0].item()
        scored.append((sim, m))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [m for _, m in scored[:5]]
