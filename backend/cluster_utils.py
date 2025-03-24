# backend/cluster_utils.py
from supabase_client import supabase
from collections import defaultdict

def cluster_memories_by_person():
    images = supabase.table("images").select("*").execute().data
    people = supabase.table("people").select("*").execute().data
    memories = supabase.table("memories").select("*").execute().data

    clusters = defaultdict(list)

    for img in images:
        for pid in (img["faces"] or []):
            person_name = next((p["name"] for p in people if p["id"] == pid), "Unknown")
            related_memories = [m for m in memories if m["image_id"] == img["id"]]
            clusters[person_name].extend(related_memories)

    return clusters
