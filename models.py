from extensions import db

class Faculty(db.Model):
    __tablename__ = 'faculties'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)

    def __init__(self, name, department, title):
        self.name = name
        self.department = department
        self.title = title

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "title": self.title
        }
