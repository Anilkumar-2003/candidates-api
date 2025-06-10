from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from models.candidate_model import candidate_serializer # type: ignore
from bson import ObjectId
import bcrypt

candidate_bp = Blueprint('candidate_bp', __name__)
client = MongoClient("mongodb+srv://anilkumar:anilkumar@ecommerce.cngsbpv.mongodb.net/?retryWrites=true&w=majority&appName=ecommerce")
db = client.job_portal
candidates_collection = db.candidates
users_collection = db.users

@candidate_bp.route('/candidates', methods=['GET'])
def get_all_candidates():
    candidates = candidates_collection.find()
    return jsonify([candidate_serializer(candidate) for candidate in candidates]), 200

@candidate_bp.route('/candidates/<id>', methods=['GET'])
def get_candidate(id):
    candidate = candidates_collection.find_one({"_id": ObjectId(id)})
    if candidate:
        return jsonify(candidate_serializer(candidate)), 200
    return jsonify({"error": "Candidate not found"}), 404

@candidate_bp.route('/candidates', methods=['POST'])
def add_candidate():
    data = request.get_json()
    new_candidate = {
        "name": data["name"],
        "role": data["role"],
        "location": data["location"],
        "experience": data["experience"],
        "skills": data["skills"],
        "salary": data["salary"],
        "availability": data["availability"],
        "rating": data["rating"],
        "image": data.get("image", "")
    }
    result = candidates_collection.insert_one(new_candidate)
    return jsonify({"id": str(result.inserted_id)}), 201

@candidate_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"error": "Name, email, and password are required"}), 400

        # Check if email already exists
        if users_collection.find_one({"email": email}):
            return jsonify({"error": "Email already registered"}), 400

        # Hash password
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Insert user
        new_user = {
            "name": name,
            "email": email,
            "password": hashed_password
        }
        result = users_collection.insert_one(new_user)
        return jsonify({"message": "Registration successful", "id": str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({"error": "Server error"}), 500

@candidate_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Find user
        user = users_collection.find_one({"email": email})
        if not user:
            return jsonify({"error": "Invalid credentials"}), 403

        # Verify password
        if bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
            return jsonify({"message": "Login successful", "user_id": str(user["_id"]), "name": user["name"]}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 403

    except Exception as e:
        return jsonify({"error": "Server error"}), 500