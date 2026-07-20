import csv
import uvicorn

from fastapi import FastAPI, HTTPException

from config import FILE_NAME
from models import Student

from student_service import (
    generate_fake_students,
    get_student_by_id
)

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
# Get All Students
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
# Get Student By ID
# ==========================================

@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = get_student_by_id(student_id)

    if student:

        return student


    raise HTTPException(
        status_code=404,
        detail="Student Not Found"
    )



# ==========================================
# Add Student
# ==========================================

@app.post("/students")
def add_student_api(student: Student):

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if int(row["id"]) == student.id:

                raise HTTPException(
                    status_code=400,
                    detail="Student ID Already Exists"
                )


    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                student.id,
                student.name,
                student.age,
                student.course,
                student.gpa
            ]
        )


    return {
        "message": "Student Added Successfully"
    }



# ==========================================
# Generate Fake Students
# ==========================================

@app.post("/students/fake")
def fake_students():

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
# ==========================================

if __name__ == "__main__":

    print("\n====================================")
    print(" Student Management System ")
    print("====================================\n")

    print("Starting Terminal Menu...\n")

    main_menu()