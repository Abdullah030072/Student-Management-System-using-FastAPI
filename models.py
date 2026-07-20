from pydantic import BaseModel


# ==========================================
# Student Model
# ==========================================

class Student(BaseModel):

    id: int
    name: str
    age: int
    course: str
    gpa: float