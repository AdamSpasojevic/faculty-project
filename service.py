from repository import FacultyRepository


class FacultyService:
    def __init__(self):
        self.repo = FacultyRepository()

    def get_all_faculties(self):
        faculties = self.repo.get_all_faculties()  # FIXED
        return [faculty.to_dict() for faculty in faculties]

    def get_faculty_by_id(self, faculty_id):
        faculty = self.repo.get_faculty_by_id(faculty_id)
        return faculty.to_dict() if faculty else None

    def create_faculty(self, name, department, title):
        faculty = self.repo.create_faculty(name, department, title)
        return faculty.to_dict()

    def update_faculty(self, faculty_id, name, department, title):
        faculty = self.repo.update_faculty(faculty_id, name, department, title)
        return faculty.to_dict() if faculty else None

    def delete_faculty(self, faculty_id):
        return self.repo.delete_faculty(faculty_id)
