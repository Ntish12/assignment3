# report_generator.py

# Sample employee data (replace this with actual data from your application)
employees = [
    {'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'department': 'HR', 'salary': 50000, 'date_of_birth': '1990-01-01', 'start_year': 2015, 'position': 'Manager'},
    {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'department': 'IT', 'salary': 60000, 'date_of_birth': '1985-05-15', 'start_year': 2017, 'position': 'Developer'},
    {'id': 3, 'first_name': 'Alice', 'last_name': 'Johnson', 'department': 'HR', 'salary': 55000, 'date_of_birth': '1988-10-20', 'start_year': 2016, 'position': 'Analyst'}
]

def list_department():
    print("\nList of Departments:")
    departments = set(employee['department'] for employee in employees)
    for department in departments:
        print(department)

def list_employees():
    print("\nList of All Employees:")
    for employee in employees:
        print(f"ID: {employee['id']}, Name: {employee['first_name']} {employee['last_name']}, Department: {employee['department']}, Position: {employee['position']}, Salary: {employee['salary']}, Start Year: {employee['start_year']}, Date of Birth: {employee['date_of_birth']}")

def average_age_and_salary_per_department():
    print("\nDepartment Statistics:")
    department_stats = {}
    for employee in employees:
        if employee['department'] not in department_stats:
            department_stats[employee['department']] = {'count': 1, 'total_salary': employee['salary'], 'oldest_age': calculate_age(employee['date_of_birth']), 'salary_sum': employee['salary']}
        else:
            department_stats[employee['department']]['count'] += 1
            department_stats[employee['department']]['total_salary'] += employee['salary']
            department_stats[employee['department']]['oldest_age'] = max(department_stats[employee['department']]['oldest_age'], calculate_age(employee['date_of_birth']))
            department_stats[employee['department']]['salary_sum'] += employee['salary']
    
    for department, stats in department_stats.items():
        avg_salary = stats['total_salary'] / stats['count']
        avg_age = stats['oldest_age']
        print(f"Department: {department}, Average Age: {avg_age}, Average Salary: {avg_salary}")

def list_employees_per_department():
    print("\nDepartment Employee Details:")
    for department in set(employee['department'] for employee in employees):
        print(f"\nEmployees in {department}:")
        for employee in employees:
            if employee['department'] == department:
                age = calculate_age(employee['date_of_birth'])
                print(f"ID: {employee['id']}, Name: {employee['first_name']} {employee['last_name']}, Department: {employee['department']}, Position: {employee['position']}, Salary: {employee['salary']}, Start Year: {employee['start_year']}, Date of Birth: {employee['date_of_birth']}, Age: {age}")

def calculate_age(date_of_birth):
    # Sample implementation for calculating age from date of birth
    # Replace this with your own implementation if needed
    # This implementation assumes date_of_birth is in 'YYYY-MM-DD' format
    import datetime
    today = datetime.date.today()
    dob = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def add_employee_to_list(employee):
    global employees
    employee_id = len(employees) + 1
    employee['id'] = employee_id
    employees.append(employee)
    print(f"Employee {employee['first_name']} {employee['last_name']} added successfully!")

# Sample usage for testing purposes
if __name__ == "__main__":
    list_department()
    list_employees()
    average_age_and_salary_per_department()
    list_employees_per_department()
