# backend/bulk_memory_import.py
from memory_manager import store_memory

def import_memories_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        clean = line.strip()
        if clean:
            print(f"🧠 Storing: {clean}")
            store_memory(clean)

if __name__ == "__main__":
    import_memories_from_txt("personal_memories.txt")
