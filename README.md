<p align="center">
  <img src="https://your-project-logo-url.com" alt="AI Memory Clone Logo" width="150"/>
</p>

<h1 align="center">🧠 AI Memory Clone</h1>

<p align="center">Personal AI with memory recall, semantic search, and image understanding — powered by local or cloud models.</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v1.0.0-purple">
  <img alt="Build" src="https://img.shields.io/badge/build-passing-brightgreen">
  <img alt="Frontend" src="https://img.shields.io/badge/frontend-React-blue">
  <img alt="Backend" src="https://img.shields.io/badge/backend-FastAPI-orange">
  <img alt="Database" src="https://img.shields.io/badge/database-SQLite%20%7C%20PostgreSQL-lightgrey">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-informational">
</p>

<p align="center">
  <a href="https://github.com/manojmadduri/ai-memory-clone"><img src="https://img.shields.io/github/stars/manojmadduri/ai-memory-clone?style=social" alt="GitHub stars"></a>
  <a href="https://discord.gg/yourlink"><img src="https://img.shields.io/discord/000000000000000000?color=7289DA&label=Discord&logo=discord&style=flat" alt="Discord"></a>
  <a href="https://twitter.com/yourhandle"><img src="https://img.shields.io/twitter/follow/yourhandle?style=social" alt="Twitter"></a>
</p>

---


```
🧠 AI Memory Clone

This project creates a personal AI that can:
- 🧠 Store and recall your memories (facts, diary entries, preferences)
- 💬 Chat like you using GPT + memory context
- 📷 Ingest and caption images with face recognition
- 🗂️ Organize memories by people, timeline, and events

---

## 🏗️ Tech Stack

- Frontend: React + Tailwind CSS
- Backend: FastAPI (Python)
- Memory Embedding: `sentence-transformers`
- Face Recognition: `face_recognition` + `dlib`
- Image Captioning: (placeholder, BLIP-like)
- LLM: OpenAI GPT or local-compatible chat model
- Database: Supabase (PostgreSQL & Storage)

---

## 📦 Installation

### ✅ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
```

**Install extra dependencies:**

```bash
pip install cmake dlib face_recognition
pip install python-multipart
```

> If you hit version conflicts:
```bash
pip install \
  sentence-transformers==2.2.2 \
  transformers==4.25.1 \
  huggingface_hub==0.13.4 \
  tokenizers==0.13.3 \
  accelerate==0.18.0
```

### ✅ Frontend Setup

```bash
cd frontend
npm install
npm start
```

> Opens at `http://localhost:3000`

---

## 🔑 Environment Variables

Create `.env` in `backend/`:

```env
SUPABASE_URL=https://yourproject.supabase.co
SUPABASE_KEY=your_public_anon_key
```

---

## 🚀 Running the App

```bash
# Backend
cd backend
uvicorn main:app --reload

# Frontend
cd frontend
npm start
```

---

## 🧠 Memory Features

### Add Memory (API)
```bash
POST /memory/add?text=I visited Manali in Jan 2022.
```

### Add Bulk Memories (diary.txt)
1. Create `personal_memories.txt` with one memory per line
2. Run:

```bash
python bulk_memory_import.py
```

### Query Memory (API)
```bash
GET /memory/query?query=When is my mom’s birthday?
```

---

## 💬 Chat with Memory

### Endpoint
```bash
POST /chat
{ "query": "What do I eat?" }
```

### Returns
```json
{
  "reply": "You prefer vegetarian food.",
  "memories": [
    "I prefer vegetarian food.",
    "I avoid whey protein in my diet."
  ]
}
```

---

## 📷 Image Ingestion (WIP)

### Upload Image
```bash
POST /image/upload
```

- Face encoding
- Caption embedding
- Uploads to Supabase Storage
- Links to memory

---

## 📄 Folder Structure

```
ai-memory-clone/
├── backend/
│   ├── main.py
│   ├── memory_manager.py
│   ├── gpt_response.py
│   ├── image_ingestion.py
│   ├── bulk_memory_import.py
│   ├── supabase_client.py
│   ├── face_utils.py
│   └── .env
├── frontend/
│   ├── src/pages/Upload.js
│   ├── src/pages/Chat.js
│   └── ...
```

---

## ✅ Features Implemented

- [x] Add single memory (API or frontend)
- [x] Bulk import from `.txt`
- [x] Store memory embeddings in Supabase
- [x] Query memories via semantic + time
- [x] Generate GPT reply using memory
- [x] Display used memories in chat UI
- [x] Upload and process image (WIP)
- [x] CORS, Axios, error fixes

---

## 🧩 Next Goals

- [ ] Real image captioning (BLIP model)
- [ ] Real-time camera integration
- [ ] Image-based memory retrieval (`who is this?`)
- [ ] Memory clustering by person/event
- [ ] OAuth + user-based memory system
- [ ] Export memories as timeline

---

## 👤 Created by: ManojMadduri 

```



