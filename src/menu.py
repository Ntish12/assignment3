"""
Menu Module
This module provides the main menu interface for the Employee Management System.
Users can interact with the application through the menu options, which include
adding, deleting, updating employee information, generating reports, and exiting
the application.
"""# main.py

from employee_operations import add_employee, delete_employee, update_employee
from report_generation import list_department, list_employees, \
    average_age_and_salary_per_department, list_employees_per_department

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Generate Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            delete_employee()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            generate_reports_menu()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def generate_reports_menu():
    while True:
        print("\nGenerate Reports")
        print("1. List of Departments")
        print("2. List of All Employees")
        print("3. Department Statistics")
        print("4. Department Employee Details")
        print("5. Back to Main Menu")

        report_choice = input("Enter your choice: ")

        if report_choice == '1':
            list_department()
        elif report_choice == '2':
            list_employees()
        elif report_choice == '3':
           average_age_and_salary_per_department()
        elif report_choice == '4':
            list_employees_per_department()
        elif report_choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

from employee_operations import add_employee, delete_employee, update_employee
from report_generation import generate_reports 

def main_menu():
    """
    Main Menu Function
    Displays the main menu for the Employee Management System and prompts the user for input.
    Based on the user's choice, it calls the corresponding functions to perform actions such as
    adding, deleting, or updating employee information, generating reports, or exiting the program.
    """
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Update Employee")
    print("4. Generate Reports")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice.isdigit():  # Check if input is a digit
        choice = int(choice)
        if choice == 1:
            add_employee()
        elif choice == 2:
            delete_employee()
        elif choice == 3:
            update_employee()
        elif choice == 4:
            generate_reports()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    else:
        print("Invalid input. Please enter a number.")

