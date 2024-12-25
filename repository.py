from extensions import db
from models import Faculty

class FacultyRepository:
    def get_all_faculties(self):
        return Faculty.query.all()

    def get_faculty_by_id(self, faculty_id):
        return Faculty.query.get(faculty_id)

    def create_faculty(self, name, department, title):
        new_faculty = Faculty(name, department, title)
        db.session.add(new_faculty)
        db.session.commit()
        return new_faculty

    def update_faculty(self, faculty_id, name, department, title):
        faculty = self.get_faculty_by_id(faculty_id)
        if faculty:
            faculty.name = name
            faculty.department = department
            faculty.title = title
            db.session.commit()
            return faculty
        return None

    def delete_faculty(self, faculty_id):
        faculty = self.get_faculty_by_id(faculty_id)
        if faculty:
            db.session.delete(faculty)
            db.session.commit()
            return True
        return False

