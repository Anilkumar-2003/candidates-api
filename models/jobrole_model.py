
from bson import ObjectId

def jobrole_serializer(jobrole) -> dict:
    return {
        "id": str(jobrole["_id"]),
        "title": jobrole["title"],
        "department": jobrole["department"],
        "location": jobrole["location"],
        "experience": jobrole["experience"],
        "salary": jobrole["salary"],
        "skills": jobrole["skills"],
        "openings": jobrole["openings"],
        "applicants": jobrole["applicants"]
    }