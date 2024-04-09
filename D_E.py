def delete_employee(employees):
   
     # to delete
    employee_id = input("Enter the ID of the employee to delete: ")
    
    # Check if the employee ID exists
    for employee in employees:
        if employee.get('id') == employee_id:
            employees.remove(employee)
            print("Employee deleted successfully!")
            return
    
    # If the ID does not exist
    print("Employee with ID '{}' not found.".format(employee_id))

# Example usage:
employees = [{'id': '1', 'name': 'John', 'age': '30', 'position': 'Manager'},
             {'id': '2', 'name': 'Alice', 'age': '25', 'position': 'Assistant'}]
delete_employee(employees)