def add_employee(employees):

    # Ask for employee details
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    position = input("Enter employee position: ")
    
    # Create a dictionary to store the details
    new_employee = {
        'name': name,
        'age': age,
        'position': position
    }
    
    # Add the new employee to the list of employees
    employees.append(new_employee)
    print("Employee added successfully!")

# Example usage:
employees = []
add_employee(employees)