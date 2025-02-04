from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from src.services.faculty_service import FacultyService
from src.repositories.faculty_repository import FacultyRepository
from src.dtos.faculty_dto import FacultyDTO

faculty_repository = FacultyRepository()  # Instantiate Repository
faculty_service = FacultyService(faculty_repository)  # Inject into Service

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
    # Grab the raw JSON
    raw_json = request.get_json()

    # Validate against the Pydantic DTO
    dto = FacultyDTO(**request.get_json())

    # Convert the DTO to a Faculty model
    faculty_obj = dto.to_model()

    # Create in DB
    new_faculty = faculty_service.create_faculty(faculty_obj)
    return jsonify(new_faculty), 201


@faculty_blueprint.route('/faculty/<int:faculty_id>', methods=['PUT'])
def update_faculty(faculty_id):
    raw_json = request.get_json()
    if not raw_json:
        return jsonify({"error": "No data provided"}), 400

    try:
        dto = FacultyDTO(**raw_json)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    faculty_obj = dto.to_model()

    updated_faculty = faculty_service.update_faculty(faculty_id, faculty_obj)
    if updated_faculty:
        return jsonify(updated_faculty), 200
    return jsonify({"error": "Faculty not found"}), 404


@faculty_blueprint.route('/faculty/<int:faculty_id>', methods=['DELETE'])
def delete_faculty(faculty_id):
    success = faculty_service.delete_faculty(faculty_id)
    if success:
        return jsonify({"message": "Faculty deleted"}), 200
    return jsonify({"error": "Faculty not found"}), 404

