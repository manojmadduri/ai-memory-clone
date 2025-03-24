# backend/face_utils.py
import face_recognition
from supabase_client import supabase
import numpy as np

def find_closest_face_encoding(face_encoding):
    people = supabase.table("people").select("*").execute().data

    best_match = None
    best_distance = float("inf")

    for person in people:
        db_encoding = np.array(person["face_encoding"])
        distance = np.linalg.norm(face_encoding - db_encoding)
        if distance < 0.5 and distance < best_distance:
            best_match = person
            best_distance = distance

    return best_match
