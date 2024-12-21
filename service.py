class FacultyService:
    # In-memory storage for demonstration
    # Each faculty: {"id": int, "name": str, "department": str, "title": str}
    _faculties = []
    _next_id = 1

    @classmethod
    def get_all_faculties(cls):
        return cls._faculties

    @classmethod
    def get_faculty_by_id(cls, faculty_id):
        return next((f for f in cls._faculties if f["id"] == faculty_id), None)

    @classmethod
    def create_faculty(cls, data):
        new_faculty = {
            "id": cls._next_id,
            "name": data["name"],
            "department": data["department"],
            "title": data["title"]
        }
        cls._faculties.append(new_faculty)
        cls._next_id += 1
        return new_faculty

    @classmethod
    def update_faculty(cls, faculty_id, data):
        faculty = cls.get_faculty_by_id(faculty_id)
        if faculty is None:
            return None
        # Update only the provided fields
        if "name" in data:
            faculty["name"] = data["name"]
        if "department" in data:
            faculty["department"] = data["department"]
        if "title" in data:
            faculty["title"] = data["title"]
        return faculty

    @classmethod
    def delete_faculty(cls, faculty_id):
        faculty = cls.get_faculty_by_id(faculty_id)
        if faculty:
            cls._faculties.remove(faculty)
            return True
        return False
