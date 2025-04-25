<p align="center">
  <img src="./logo.png" alt="AI Memory Clone Logo" width="150"/>
</p>

<h1 align="center">🧠 AI Memory Clone</h1>

<p align="center">Personal AI with memory recall, semantic search, and image understanding — powered by local or cloud models.</p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v2.0.0-purple">
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
Sure! Here's your updated `README.md` so far, based on your current project structure and features:

---

### 🧠 AI Memory Clone Chatbot (Offline, Private)

This is a **fully offline**, privacy-first AI chatbot that remembers past events and responds based on stored memory. It uses **local embeddings, SQLite**, and **Ollama for local LLM inference** (e.g., Mistral, LLaMA).

---

### ✅ Features

- 🧠 Memory-based responses (stored and retrieved locally)
- 💬 Chat interface with history
- ⚡ Local LLM via [Ollama](https://ollama.com/) (e.g., `mistral`, `llama2`, etc.)
- 📦 Fast and lightweight: uses SQLite + local vector store
- 🔒 100% private (no OpenAI, no internet needed)
- ✅ Memory ingestion & search
- ❌ Does **not** show “memories used” in UI (customizable)

---

### 🏗️ Tech Stack

- **Frontend**: React + Axios
- **Backend**: Python (FastAPI / Flask recommended)
- **LLM**: Ollama (`mistral`, `llama2`, etc.)
- **Embedding**: `sentence-transformers` or `InstructorTransformer`
- **Vector Store**: FAISS
- **Database**: SQLite

---

### 🚀 Setup Instructions

#### 1. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then pull the model:

```bash
ollama pull mistral
```

#### 2. Backend Setup (Python)

```bash
pip install -r requirements.txt
```

Create `.env` if needed (optional for local paths).

Start the backend:

```bash
python app.py
```

This starts the API at `http://localhost:8000`.

#### 3. Frontend Setup (React)

```bash
npm install
npm start
```

This starts the app at `http://localhost:3000`.

---

### 📁 Folder Structure

```
/backend
  ├── app.py
  ├── memory_manager.py
  └── embeddings/
      └── vector_store.faiss

/frontend
  ├── Chat.js
  ├── App.js
  └── index.js
```

---

### 📌 Endpoints

- `POST /chat`  
  Sends user query and returns LLM response (with memory injection internally)

---

### 🧠 Memory Example (Not Shown in UI)

- "My mom's birthday is June 5th."
- "I visited Manali in Jan 2022."
- "I prefer vegetarian food."

---
