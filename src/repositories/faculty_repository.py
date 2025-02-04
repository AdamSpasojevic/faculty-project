from src.extensions import db
from src.models.faculty import Faculty

class FacultyRepository:

    def get_all_faculties(self):
        return Faculty.query.all()

    def get_faculty_by_id(self, faculty_id):
        return Faculty.query.get(faculty_id)

    def create_faculty(self, faculty_obj: Faculty):
        """
        Accept a Faculty object, add & commit to DB, return the Faculty.
        """
        db.session.add(faculty_obj)
        db.session.commit()
        return faculty_obj

    def update_faculty(self, faculty_obj: Faculty):
        """
        Accept a *Faculty* object (with an existing ID), update DB, commit, return updated faculty.
        """
        existing_faculty = Faculty.query.get(faculty_obj.id)
        if existing_faculty:
            existing_faculty.name = faculty_obj.name
            existing_faculty.department = faculty_obj.department
            existing_faculty.title = faculty_obj.title
            db.session.commit()
            return existing_faculty
        return None

    def delete_faculty(self, faculty_id):
        faculty = self.get_faculty_by_id(faculty_id)
        if faculty:
            db.session.delete(faculty)
            db.session.commit()
            return True
        return False
