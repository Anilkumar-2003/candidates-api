
from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from models.jobrole_model import jobrole_serializer
from bson import ObjectId

jobrole_bp = Blueprint('jobrole_bp', __name__)
client = MongoClient("mongodb://localhost:27017/")
db = client.job_portal
jobroles_collection = db.jobroles

@jobrole_bp.route('/job-roles', methods=['GET'])
def get_all_jobroles():
    jobroles = jobroles_collection.find()
    return jsonify([jobrole_serializer(job) for job in jobroles]), 200

@jobrole_bp.route('/job-roles/<id>', methods=['GET'])
def get_jobrole(id):
    job = jobroles_collection.find_one({"_id": ObjectId(id)})
    if job:
        return jsonify(jobrole_serializer(job)), 200
    return jsonify({"error": "Job role not found"}), 404
