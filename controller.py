from flask import Blueprint, request, jsonify

# Create a blueprint for the faculty endpoints
faculty_blueprint = Blueprint('faculty', __name__)

@faculty_blueprint.route('/faculty', methods=['GET'])
def get_all_faculties():
    """
    Retrieve all faculty records.
    """
    faculties = faculty_service.get_all_faculties()
    return jsonify(faculties), 200


@faculty_blueprint.route('/faculty/<int:faculty_id>', methods=['GET'])
def get_faculty(faculty_id):
    """
    Retrieve a specific faculty by ID.
    """
    faculty = faculty_service.get_faculty_by_id(faculty_id)
    if faculty:
        return jsonify(faculty), 200
    return jsonify({"error": "Faculty not found"}), 404