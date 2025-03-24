# backend/timeline_utils.py
from supabase_client import supabase
from collections import defaultdict
from datetime import datetime

def group_memories_by_timeline(granularity="day"):
    memories = supabase.table("memories").select("*").execute().data
    grouped = defaultdict(list)

    for mem in memories:
        dt = datetime.fromisoformat(mem["timestamp"].replace("Z", "")) if "Z" in mem["timestamp"] else datetime.fromisoformat(mem["timestamp"])
        if granularity == "day":
            key = dt.strftime("%Y-%m-%d")
        elif granularity == "month":
            key = dt.strftime("%Y-%m")
        elif granularity == "week":
            key = dt.strftime("%Y-W%U")
        else:
            key = "unknown"
        grouped[key].append(mem)

    return grouped
