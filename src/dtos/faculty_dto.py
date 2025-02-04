from pydantic import BaseModel


class FacultyDTO(BaseModel):
    name: str
    department: str
    title: str

    def to_model(self):
        from src.models.faculty import Faculty
        return Faculty(name=self.name, department=self.department, title=self.title)
