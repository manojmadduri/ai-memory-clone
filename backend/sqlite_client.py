import sqlite3
import json

conn = sqlite3.connect("memories.db", check_same_thread=False)
cursor = conn.cursor()

# ✅ Create updated schema
cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content TEXT NOT NULL,
    embedding TEXT NOT NULL,
    tags TEXT,
    image_id TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def insert_memory(text, embedding, tags=None, image_id=None):
    cursor.execute(
        "INSERT INTO memories (content, embedding, tags, image_id) VALUES (?, ?, ?, ?)",
        (text, json.dumps(embedding), json.dumps(tags), image_id)
    )
    conn.commit()

def fetch_all_memories():
    cursor.execute("SELECT content, embedding FROM memories")
    rows = cursor.fetchall()
    return [{"text": row[0], "embedding": row[1]} for row in rows]
