from src.repositories.faculty_repository import FacultyRepository
from src.models.faculty import Faculty


class FacultyService:
    def __init__(self, faculty_repository: FacultyRepository):
        self.repo = faculty_repository

    def get_all_faculties(self):
        faculties = self.repo.get_all_faculties()
        return [f.to_dict() for f in faculties]

    def get_faculty_by_id(self, faculty_id):
        faculty = self.repo.get_faculty_by_id(faculty_id)
        return faculty.to_dict() if faculty else None

    def create_faculty(self, faculty: Faculty):
        created = self.repo.create_faculty(faculty)
        return created.to_dict()

    def update_faculty(self, updated_faculty: Faculty):
        if updated_faculty.id is None:
            return None  # Ensure faculty object has an ID

        existing = self.repo.get_faculty_by_id(updated_faculty.id)
        if not existing:
            return None

        saved = self.repo.update_faculty(updated_faculty)
        return saved.to_dict() if saved else None

    def delete_faculty(self, faculty_id: int):
        return self.repo.delete_faculty(faculty_id)

