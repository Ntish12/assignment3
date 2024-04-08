
# Employee Operations Module
class Employee:
    def __init__(self, id, first_name, last_name, date_of_birth, start_year, position, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.start_year = start_year
        self.position = position
        self.salary = salary
employees = [
    Employee(1, 'John', 'Doe', '1980-01-01', 2000, 'Manager', 80000),
    Employee(2, 'Jane', 'Smith', '1985-02-15', 2010, 'Developer', 70000),
    Employee(3, 'Mike', 'Johnson', '1990-05-10', 2015, 'Designer', 60000)
]
def add_employee():
    # Add Employee Function
    # input details for a new employee and adds the employee
    id = int(input("Enter the ID for the new employee: "))
    first_name = input("Enter the first name for the new employee: ")
    last_name = input("Enter the last name for the new employee: ")
    date_of_birth = input("Enter the date of birth for the new employee (YYYY-MM-DD): ")
    start_year = int(input("Enter the start year for the new employee: "))
    position = input("Enter the position for the new employee: ")
    salary = float(input("Enter the salary for the new employee: "))
    new_employee = Employee(id, first_name, last_name, date_of_birth, start_year, position, salary)
    employees.append(new_employee)
    print(f"Employee {new_employee.first_name} {new_employee.last_name} added to the system.")

def delete_employee():
    # Delete Employee Function
    # input the ID of the employee to be deleted and
    # removes the employee from the system.
    id = int(input("Enter the ID of the employee to be deleted: "))
    for employee in employees:
        if employee.id == id:
            employees.remove(employee)
            print(f"Employee with ID {id} deleted from the system.")
            return
    print(f"No employee with ID {id} found in the system.")

def update_employee():
    # Update Employee Function
    # input the ID of the employee to be updated and allows the user to modify the employee's information such as name, department, or salary.

    id = int(input("Enter the ID of the employee to be updated: "))
    for employee in employees:
        if employee.id == id:
            first_name = input("Enter the new first name for the employee: ")
            last_name = input("Enter the new last name for the employee: ")
            date_of_birth = input("Enter the new date of birth for the employee (YYYY-MM-DD): ")
            start_year = int(input("Enter the new start year for the employee: "))
            position = input("Enter the new position for the employee: ")
            salary = float(input("Enter the new salary for the employee: "))

            employee.first_name = first_name
            employee.last_name = last_name
            employee.date_of_birth = date_of_birth
            employee.start_year = start_year
            employee.position = position
            employee.salary = salary

            print(f"Employee with ID {id} updated.")
            return

    print(f"No employee with ID {id} found in the system.")