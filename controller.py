from flask import Blueprint, request, jsonify
from service import FacultyService

faculty_blueprint = Blueprint('faculty', __name__)


@faculty_blueprint.route("/faculty", methods=["GET"])
def get_all_faculties():
    faculties = FacultyService.get_all_faculties()
    return jsonify(faculties), 200


@faculty_blueprint.route("/faculty/<int:faculty_id>", methods=["GET"])
def get_faculty(faculty_id):
    faculty = FacultyService.get_faculty_by_id(faculty_id)
    if faculty:
        return jsonify(faculty), 200
    return jsonify({"error": "Faculty not found"}), 404


@faculty_blueprint.route("/faculty", methods=["POST"])
def create_faculty():
    data = request.get_json()
    if not data or "name" not in data or "department" not in data or "title" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    new_faculty = FacultyService.create_faculty(data)
    return jsonify(new_faculty), 201


@faculty_blueprint.route("/faculty/<int:faculty_id>", methods=["PUT"])
def update_faculty(faculty_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    updated_faculty = FacultyService.update_faculty(faculty_id, data)
    if updated_faculty:
        return jsonify(updated_faculty), 200
    return jsonify({"error": "Faculty not found"}), 404


@faculty_blueprint.route("/faculty/<int:faculty_id>", methods=["DELETE"])
def delete_faculty(faculty_id):
    success = FacultyService.delete_faculty(faculty_id)
    if success:
        return '', 204
    return jsonify({"error": "Faculty not found"}), 404
