from database import create_file

from student_service import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
    generate_fake_students
)


# ==========================================
# Main Menu
# ==========================================

def main_menu():

    create_file()

    while True:

        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Generate 50 Fake Students")
        print("7. Exit")

        choice = input("\nEnter Your Choice: ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            generate_fake_students()

        elif choice == "7":

            print("\nThank You for Using Student Management System.")
            print("Good Bye!")

            break

        else:

            print("\nInvalid Choice! Please Try Again.\n")