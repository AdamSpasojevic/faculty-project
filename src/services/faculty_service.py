from src.repositories.faculty_repository import FacultyRepository
from src.models.faculty import Faculty


class FacultyService:
    def __init__(self):
        self.repo = FacultyRepository()

    def get_all_faculties(self):
        faculties = self.repo.get_all_faculties()
        return [f.to_dict() for f in faculties]

    def get_faculty_by_id(self, faculty_id):
        faculty = self.repo.get_faculty_by_id(faculty_id)
        return faculty.to_dict() if faculty else None

    def create_faculty(self, faculty: Faculty):
        created = self.repo.create_faculty(faculty)
        return created.to_dict()

    def update_faculty(self, faculty_id: int, updated_faculty: Faculty):
        """
        1) Use faculty_id to check if record exists
        2) If yes, set updated_faculty.id so the repository can do the merge
        """
        existing = self.repo.get_faculty_by_id(faculty_id)
        if not existing:
            return None

        updated_faculty.id = faculty_id

        saved = self.repo.update_faculty(updated_faculty)
        return saved.to_dict() if saved else None

    def delete_faculty(self, faculty_id: int):
        return self.repo.delete_faculty(faculty_id)
