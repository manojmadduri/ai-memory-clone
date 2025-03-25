from fastapi import FastAPI, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from memory_manager import store_memory, query_memories
from image_ingestion import process_image
from cluster_utils import cluster_memories_by_person
from gpt_response import generate_reply_with_memory
from timeline_utils import group_memories_by_timeline
import shutil
import os

app = FastAPI()

# ✅ Correct CORS middleware added BEFORE any route definitions
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/memory/add")
async def add_memory(text: str):
    store_memory(text)
    return {"status": "added"}

@app.get("/memory/query")
async def search_memory(query: str, time: str = None):
    results = query_memories(query, time_filter=time)
    return {"results": results}

@app.get("/memory/by-person")
async def by_person():
    return cluster_memories_by_person()

@app.get("/memory/by-timeline")
async def by_time(granularity: str = "day"):
    return group_memories_by_timeline(granularity)

@app.post("/image/upload")
async def upload_image(file: UploadFile):
    try:
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        process_image(temp_path)
        os.remove(temp_path)

        return {"status": "image processed"}

    except Exception as e:
        print("❌ Upload failed:", e)
        return {"error": str(e)}


@app.post("/chat")
async def chat_with_memory(request: Request):
    body = await request.json()
    query = body.get("query", "")
    response = generate_reply_with_memory(query)
    return response  # ✅ Not wrapped in { "reply": response }

