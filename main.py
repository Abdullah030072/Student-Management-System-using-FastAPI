import csv
<<<<<<< HEAD
import uvicorn

from fastapi import FastAPI, HTTPException

from config import FILE_NAME
from models import Student

from student_service import (
    generate_fake_students,
    get_student_by_id
)

from menu import main_menu



=======

from fastapi import FastAPI

from config import FILE_NAME
from models import Student
from menu import main_menu


>>>>>>> origin/fastapi
# ==========================================
# FastAPI App
# ==========================================

app = FastAPI(
    title="Student Management System Using FastAPI",
    description="API for Managing Student Records",
    version="1.0.0"
)


<<<<<<< HEAD

=======
>>>>>>> origin/fastapi
# ==========================================
# Home API
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to Student Management System API"
    }


<<<<<<< HEAD

# ==========================================
# Get All Students
=======
# ==========================================
# View All Students
>>>>>>> origin/fastapi
# ==========================================

@app.get("/students")
def get_students():

    students = []

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            students.append(row)

    return students


<<<<<<< HEAD

# ==========================================
# Get Student By ID
=======
# ==========================================
# Search Student By ID
>>>>>>> origin/fastapi
# ==========================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

<<<<<<< HEAD
    student = get_student_by_id(student_id)

    if student:

        return student


    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )

=======
    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if int(row["ID"]) == student_id:

                return row

    return {
        "message": "Student Not Found"
    }
>>>>>>> origin/fastapi


# ==========================================
# Add Student
# ==========================================

@app.post("/students")
def add_student_api(student: Student):

    with open(FILE_NAME, "r") as file:

<<<<<<< HEAD
        reader = csv.DictReader(file)

        for row in reader:

            if int(row["id"]) == student.id:

                raise HTTPException(
                    status_code=400,
                    detail="Student ID Already Exists"
                )

=======
        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and int(row[0]) == student.id:

                return {
                    "message": "Student ID Already Exists"
                }
>>>>>>> origin/fastapi

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

<<<<<<< HEAD
        writer.writerow(
            [
                student.id,
                student.name,
                student.age,
                student.course,
                student.gpa
            ]
        )

=======
        writer.writerow([
            student.id,
            student.name,
            student.age,
            student.course,
            student.gpa
        ])
>>>>>>> origin/fastapi

    return {
        "message": "Student Added Successfully"
    }


<<<<<<< HEAD

=======
>>>>>>> origin/fastapi
# ==========================================
# Generate Fake Students
# ==========================================

@app.post("/students/fake")
def fake_students():

<<<<<<< HEAD
=======
    from student_service import generate_fake_students

>>>>>>> origin/fastapi
    generate_fake_students()

    return {
        "message": "50 Fake Students Added Successfully"
    }


<<<<<<< HEAD

=======
>>>>>>> origin/fastapi
# ==========================================
# Update Student
# ==========================================

@app.put("/students/{student_id}")
def update_student_api(student_id: int, student: Student):

    rows = []

    found = False

<<<<<<< HEAD

=======
>>>>>>> origin/fastapi
    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        rows.append(header)

<<<<<<< HEAD

=======
>>>>>>> origin/fastapi
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

<<<<<<< HEAD

            rows.append(row)


    if not found:

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )


    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)


    return {
        "message": "Student Updated Successfully"
    }



=======
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


>>>>>>> origin/fastapi
# ==========================================
# Delete Student
# ==========================================

@app.delete("/students/{student_id}")
def delete_student_api(student_id: int):

    rows = []

    found = False

<<<<<<< HEAD

=======
>>>>>>> origin/fastapi
    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        rows.append(header)

<<<<<<< HEAD

=======
>>>>>>> origin/fastapi
        for row in reader:

            if int(row[0]) == student_id:

                found = True

                continue

<<<<<<< HEAD

            rows.append(row)



    if not found:

        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )


    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)


    return {
        "message": "Student Deleted Successfully"
    }




# ==========================================
# Run Terminal Menu OR FastAPI
=======
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
>>>>>>> origin/fastapi
# ==========================================

if __name__ == "__main__":

<<<<<<< HEAD
    print("\n====================================")
    print(" Student Management System ")
    print("====================================\n")

    print("Starting Terminal Menu...\n")

=======
>>>>>>> origin/fastapi
    main_menu()