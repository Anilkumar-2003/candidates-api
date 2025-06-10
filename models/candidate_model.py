# models/candidate_model.py
from bson import ObjectId

def candidate_serializer(candidate) -> dict:
    return {
        "id": str(candidate["_id"]),
        "name": candidate["name"],
        "role": candidate["role"],
        "location": candidate["location"],
        "experience": candidate["experience"],
        "skills": candidate["skills"],
        "salary": candidate["salary"],
        "availability": candidate["availability"],
        "rating": candidate["rating"],
        "image": candidate.get("image", "")
    }
