from PIL import Image
import requests
from io import BytesIO
import face_recognition
from torchvision import transforms
from supabase_client import supabase
from sentence_transformers import SentenceTransformer
import uuid
import os
from face_utils import find_closest_face_encoding


blip_model = SentenceTransformer("clip-ViT-B-32")  # Approx for image caption embedding
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def caption_image(img_path):
    return f"Image of {os.path.basename(img_path)}"  # Replace with BLIP model later

def process_image(img_path):
    image = face_recognition.load_image_file(img_path)
    face_encodings = face_recognition.face_encodings(image)

    face_ids = []
    for enc in face_encodings:
        match = find_closest_face_encoding(enc)
        if match:
            person_id = match["id"]
        else:
            person_id = str(uuid.uuid4())
            supabase.table("people").insert({
                "id": person_id,
                "name": "Unknown",
                "face_encoding": enc.tolist()
            }).execute()
        face_ids.append(person_id)

    caption = caption_image(img_path)
    embedding = blip_model.encode(caption).tolist()

    # Upload image to Supabase Storage
    with open(img_path, "rb") as f:
        filename = f"{uuid.uuid4()}.jpg"
        supabase.storage().from_("memories").upload(filename, f)

    image_url = f"{os.getenv('SUPABASE_URL')}/storage/v1/object/public/memories/{filename}"

    # Save to images table
    image_insert = supabase.table("images").insert({
        "url": image_url,
        "caption": caption,
        "faces": face_ids
    }).execute()

    image_id = image_insert.data[0]["id"]

    # Store as memory too
    from memory_manager import store_memory
    store_memory(caption, tags=["image"], image_id=image_id)
