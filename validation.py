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

        elif not name.replace(" ", "").isalpha():
            print("Name should contain only alphabets.")

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

        elif int(age) < 1 or int(age) > 100:
            print("Age must be between 1 and 100.")

        else:
            return int(age)


# ==========================================
# Validate Course
# ==========================================

def valid_course():

    while True:

        course = input("Enter Course: ").strip()

        if course == "":
            print("Course cannot be empty.")

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
                return gpa

        except ValueError:
            print("Enter a valid GPA.")