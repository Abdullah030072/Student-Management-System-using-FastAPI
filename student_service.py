import csv
import random

from config import FILE_NAME, fake, COURSES
from validation import (
    valid_id,
    valid_name,
    valid_age,
    valid_course,
    valid_gpa
)


# ==========================================
# Add Student
# ==========================================

def add_student():

    student_id = valid_id()

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if len(row) > 0 and row[0] == str(student_id):

                print("\nStudent ID Already Exists.\n")

                return

    name = valid_name()
    age = valid_age()
    course = valid_course()
    gpa = valid_gpa()

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            age,
            course,
            gpa
        ])

    print("\nStudent Added Successfully.\n")


# ==========================================
# View Students
# ==========================================

def view_students():

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        print("\n-------------------------------------------------------------")
        print("ID\tName\tAge\tCourse\tGPA")
        print("-------------------------------------------------------------")

        found = False

        for row in reader:

            found = True

            print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

        if not found:

            print("No Student Record Found.")

        print("-------------------------------------------------------------")


# ==========================================
# Search Student
# ==========================================

def search_student():

    student_id = valid_id()

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if row[0] == str(student_id):

                print("\n========== Student Found ==========")
                print("ID     :", row[0])
                print("Name   :", row[1])
                print("Age    :", row[2])
                print("Course :", row[3])
                print("GPA    :", row[4])

                return

    print("\nStudent Not Found.\n")


# ==========================================
# Update Student
# ==========================================

def update_student():

    student_id = valid_id()

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        rows.append(header)

        for row in reader:

            if row[0] == str(student_id):

                found = True

                print("\nPress Enter to Keep Old Value.\n")

                new_name = input(f"New Name ({row[1]}): ").strip()

                if new_name != "":
                    row[1] = new_name

                new_age = input(f"New Age ({row[2]}): ").strip()

                if new_age != "":
                    row[2] = new_age

                new_course = input(f"New Course ({row[3]}): ").strip()

                if new_course != "":
                    row[3] = new_course

                new_gpa = input(f"New GPA ({row[4]}): ").strip()

                if new_gpa != "":
                    row[4] = new_gpa

            rows.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        print("\nStudent Updated Successfully.\n")

    else:

        print("\nStudent Not Found.\n")


# ==========================================
# Delete Student
# ==========================================

def delete_student():

    student_id = valid_id()

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        header = next(reader)

        rows.append(header)

        for row in reader:

            if row[0] == str(student_id):

                found = True

                continue

            rows.append(row)

    if found:

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)

        print("\nStudent Deleted Successfully.\n")

    else:

        print("\nStudent Not Found.\n")


# ==========================================
# Generate 50 Fake Students
# ==========================================

def generate_fake_students():

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        existing_ids = {row[0] for row in reader if row}

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        count = 0

        while count < 50:

            student_id = random.randint(1000, 9999)

            if str(student_id) in existing_ids:

                continue

            existing_ids.add(str(student_id))

            writer.writerow([
                student_id,
                fake.name(),
                random.randint(18, 30),
                random.choice(COURSES),
                round(random.uniform(2.0, 4.0), 2)
            ])

            count += 1

    print("\n50 Fake Students Added Successfully.\n")