from config import COURSES


# ==========================================
# Validate Student ID
# ==========================================

def valid_id():

    while True:

        student_id = input("Enter Student ID: ").strip()

        if student_id == "":
            print("Student ID cannot be empty.")

        elif not student_id.isdigit():
            print("Student ID must contain only numbers.")

        elif int(student_id) <= 0:
            print("Student ID must be greater than 0.")

        else:
            return int(student_id)


# ==========================================
# Validate Student Name
# ==========================================

def valid_name():

    while True:

        name = input("Enter Name: ").strip()

        if name == "":
            print("Name cannot be empty.")

        elif len(name) < 3:
            print("Name must contain at least 3 characters.")

        elif not all(char.isalpha() or char.isspace() for char in name):
            print("Name should contain only alphabets and spaces.")

        else:
            return name


# ==========================================
# Validate Student Age
# ==========================================

def valid_age():

    while True:

        age = input("Enter Age: ").strip()

        if age == "":
            print("Age cannot be empty.")

        elif not age.isdigit():
            print("Age must be numeric.")


        else:
            return int(age)


# ==========================================
# Validate Course
# ==========================================

def valid_course():

    while True:

        print("\nAvailable Courses:")

        for course in COURSES:
            print("-", course)

        course = input("\nEnter Course: ").strip()

        if course == "":
            print("Course cannot be empty.")

        elif course not in COURSES:
            print("Invalid Course! Please choose from the list above.")

        else:
            return course


# ==========================================
# Validate GPA
# ==========================================

def valid_gpa():

    while True:

        gpa = input("Enter GPA (0-4): ").strip()

        if gpa == "":
            print("GPA cannot be empty.")
            continue

        try:

            gpa = float(gpa)

            if gpa < 0:
                print("GPA cannot be negative.")

            elif gpa > 4:
                print("GPA cannot be greater than 4.")

            else:
                return round(gpa, 2)

        except ValueError:
            print("Enter a valid GPA.")