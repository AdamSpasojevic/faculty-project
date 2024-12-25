from flask import Blueprint, request, jsonify
from service import FacultyService

faculty_service = FacultyService()
faculty_blueprint = Blueprint('faculty', __name__)


@faculty_blueprint.route('/faculty', methods=['GET'])
def get_all_faculties():
    faculties = faculty_service.get_all_faculties()
    return jsonify(faculties), 200


@faculty_blueprint.route('/faculty/<int:faculty_id>', methods=['GET'])
def get_faculty(faculty_id):
    faculty = faculty_service.get_faculty_by_id(faculty_id)
    if faculty:
        return jsonify(faculty), 200
    return jsonify({"error": "Faculty not found"}), 404


@faculty_blueprint.route('/faculty', methods=['POST'])
def create_faculty():
    data = request.get_json()
    if not data or 'name' not in data or 'department' not in data or 'title' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_faculty = faculty_service.create_faculty(
        data['name'],
        data['department'],
        data['title']
    )
    return jsonify(new_faculty), 201


@faculty_blueprint.route('/faculty/<int:faculty_id>', methods=['PUT'])
def update_faculty(faculty_id):
    data = request.get_json()
    if not data or 'name' not in data or 'department' not in data or 'title' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    updated_faculty = faculty_service.update_faculty(
        faculty_id,
        data['name'],
        data['department'],
        data['title']
    )
    if updated_faculty:
        return jsonify(updated_faculty), 200
    return jsonify({"error": "Faculty not found"}), 404


@faculty_blueprint.route('/faculty/<int:faculty_id>', methods=['DELETE'])
def delete_faculty(faculty_id):
    success = faculty_service.delete_faculty(faculty_id)
    if success:
        return jsonify({"message": "Faculty deleted"}), 200
    return jsonify({"error": "Faculty not found"}), 404
