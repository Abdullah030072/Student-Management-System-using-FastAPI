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

        next(reader)

        for row in reader:

            if row[0] == str(student_id):

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
<<<<<<< HEAD
=======



>>>>>>> origin/main
# ==========================================
# View Students
# ==========================================

def view_students():

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        print("\n-----------------------------------------------------------------------")
        print("ID\tName\t\t\tAge\tCourse\t\t\tGPA")
        print("-----------------------------------------------------------------------")


        found = False


        for row in reader:

            if len(row) != 5:
                continue

            found = True

            print(
                f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}"
            )
<<<<<<< HEAD
=======

>>>>>>> origin/main

        if not found:

            print("No Student Record Found.")

<<<<<<< HEAD
        print("-----------------------------------------------------------------------")
=======

        print("-------------------------------------------------------------")
>>>>>>> origin/main



# ==========================================
# Search Student
# ==========================================

def search_student():

    student_id = valid_id()


    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)


        for row in reader:

            if len(row) != 5:
                continue

            if row[0] == str(student_id):

                print("\n========== Student Found ==========")
<<<<<<< HEAD
                print(f"ID     : {row[0]}")
                print(f"Name   : {row[1]}")
                print(f"Age    : {row[2]}")
                print(f"Course : {row[3]}")
                print(f"GPA    : {row[4]}")
=======

                print("ID     :", row[0])
                print("Name   :", row[1])
                print("Age    :", row[2])
                print("Course :", row[3])
                print("GPA    :", row[4])
>>>>>>> origin/main

                return


    print("\nStudent Not Found.\n")
<<<<<<< HEAD
=======



>>>>>>> origin/main
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

<<<<<<< HEAD
            if len(row) != 5:
                continue
=======
>>>>>>> origin/main

            if row[0] == str(student_id):

                found = True


                print("\nPress Enter to Keep Old Value.\n")

<<<<<<< HEAD
                # =============================
                # Update Name
                # =============================

                while True:

                    new_name = input(f"New Name ({row[1]}): ").strip()

                    if new_name == "":
                        break

                    if len(new_name) < 3:

                        print("Name must contain at least 3 characters.")
                        continue

                    if not all(char.isalpha() or char.isspace() for char in new_name):

                        print("Name should contain only alphabets and spaces.")
                        continue

=======

                new_name = input(
                    f"New Name ({row[1]}): "
                ).strip()

                if new_name:
>>>>>>> origin/main
                    row[1] = new_name
                    break

<<<<<<< HEAD
                # =============================
                # Update Age
                # =============================

                while True:

                    new_age = input(f"New Age ({row[2]}): ").strip()

                    if new_age == "":
                        break

                    if not new_age.isdigit():

                        print("Age must be numeric.")
                        continue

                    if int(new_age) < 18 or int(new_age) > 30:

                        print("Age must be between 18 and 30.")
                        continue

=======


                new_age = input(
                    f"New Age ({row[2]}): "
                ).strip()

                if new_age:
>>>>>>> origin/main
                    row[2] = new_age
                    break

<<<<<<< HEAD
                # =============================
                # Update Course
                # =============================

                while True:

                    print("\nAvailable Courses:")

                    for course in COURSES:
                        print("-", course)

                    new_course = input(f"\nNew Course ({row[3]}): ").strip()

                    if new_course == "":
                        break

                    if new_course not in COURSES:

                        print("Invalid Course.")
                        continue

=======


                new_course = input(
                    f"New Course ({row[3]}): "
                ).strip()

                if new_course:
>>>>>>> origin/main
                    row[3] = new_course
                    break

<<<<<<< HEAD
                # =============================
                # Update GPA
                # =============================

                while True:

                    new_gpa = input(f"New GPA ({row[4]}): ").strip()

                    if new_gpa == "":
                        break

                    try:

                        value = float(new_gpa)

                    except ValueError:

                        print("Enter a valid GPA.")
                        continue

                    if value < 0 or value > 4:

                        print("GPA must be between 0 and 4.")
                        continue

                    row[4] = round(value, 2)
                    break
=======


                new_gpa = input(
                    f"New GPA ({row[4]}): "
                ).strip()

                if new_gpa:
                    row[4] = new_gpa
>>>>>>> origin/main



            rows.append(row)



    if found:

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerows(rows)


        print("\nStudent Updated Successfully.\n")


    else:

        print("\nStudent Not Found.\n")
<<<<<<< HEAD
=======



>>>>>>> origin/main
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

<<<<<<< HEAD
            if len(row) != 5:
                continue
=======
>>>>>>> origin/main

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

<<<<<<< HEAD
        next(reader)

        existing_ids = {row[0] for row in reader if len(row) == 5}
=======
        existing_ids = {
            row[0]
            for row in reader
            if row
        }


>>>>>>> origin/main

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)


        count = 0


        while count < 50:


            student_id = random.randint(1000,9999)


            if str(student_id) in existing_ids:
                continue


            existing_ids.add(str(student_id))


            writer.writerow([

                student_id,
                fake.name(),
                random.randint(18,30),
                random.choice(COURSES),
                round(random.uniform(2.0,4.0),2)

            ])


            count += 1

<<<<<<< HEAD
    print("\n50 Fake Students Added Successfully.\n")


=======


    print("\n50 Fake Students Added Successfully.\n")



>>>>>>> origin/main
# ==========================================
# Get Single Student (FastAPI)
# ==========================================

def get_student_by_id(student_id: int):


    with open(FILE_NAME, "r") as file:


        reader = csv.DictReader(file)


        for row in reader:

<<<<<<< HEAD
            try:

                if int(row["id"]) == student_id:

                    return {
                        "id": int(row["id"]),
                        "name": row["name"],
                        "age": int(row["age"]),
                        "course": row["course"],
                        "gpa": float(row["gpa"])
                    }

            except (KeyError, ValueError):
                continue
=======

            if int(row["id"]) == student_id:


                return {

                    "id": int(row["id"]),

                    "name": row["name"],

                    "age": int(row["age"]),

                    "course": row["course"],

                    "gpa": float(row["gpa"])

                }


>>>>>>> origin/main

    return None