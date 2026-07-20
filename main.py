import csv

from fastapi import FastAPI

from config import FILE_NAME
from models import Student
from menu import main_menu


# ==========================================
# FastAPI App
# ==========================================

app = FastAPI(
    title="Student Management System Using FastAPI",
    description="API for Managing Student Records",
    version="1.0.0"
)


# ==========================================
# Home API
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to Student Management System API"
    }


# ==========================================
# View All Students
# ==========================================

@app.get("/students")
def get_students():

    students = []

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            students.append(row)

    return students


# ==========================================
# Search Student By ID
# ==========================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if int(row["ID"]) == student_id:

                return row

    return {
        "message": "Student Not Found"
    }


# ==========================================
# Add Student
# ==========================================

@app.post("/students")
def add_student_api(student: Student):

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and int(row[0]) == student.id:

                return {
                    "message": "Student ID Already Exists"
                }

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            student.id,
            student.name,
            student.age,
            student.course,
            student.gpa
        ])

    return {
        "message": "Student Added Successfully"
    }


# ==========================================
# Generate Fake Students
# ==========================================

@app.post("/students/fake")
def fake_students():

    from student_service import generate_fake_students

    generate_fake_students()

    return {
        "message": "50 Fake Students Added Successfully"
    }


# ==========================================
# Update Student
# ==========================================

@app.put("/students/{student_id}")
def update_student_api(student_id: int, student: Student):

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        rows.append(header)

        for row in reader:

            if int(row[0]) == student_id:

                found = True

                row = [
                    student.id,
                    student.name,
                    student.age,
                    student.course,
                    student.gpa
                ]

            rows.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        return {
            "message": "Student Updated Successfully"
        }

    return {
        "message": "Student Not Found"
    }


# ==========================================
# Delete Student
# ==========================================

@app.delete("/students/{student_id}")
def delete_student_api(student_id: int):

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        rows.append(header)

        for row in reader:

            if int(row[0]) == student_id:

                found = True

                continue

            rows.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        return {
            "message": "Student Deleted Successfully"
        }

    return {
        "message": "Student Not Found"
    }


# ==========================================
# Run Terminal Program
# ==========================================

if __name__ == "__main__":

    main_menu()