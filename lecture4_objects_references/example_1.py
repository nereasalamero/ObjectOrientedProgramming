# Author:       Nerea Salamero Labara
# Date:         19/02/2025
# File:         example_3.py
# Description:  Aggregation example.

class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def display_info(self):
        print(f"Employee {self.name} (ID: {self.employee_id})")

class Department:
    def __init__(self, name):
        self.name = name
    
    def add_employee(self, employee):
        self.employees.append(employee)

    def display_info(self):
        print(f"Employees in the {self.name} department:")
        for employee in self.employees:
            employee.display_info()


employee1 = Employee("name 1", 101)
employee2 = Employee("name 2", 102)
employee3 = Employee("name 3", 103)

hr_department = Department("HR")
hr_department.add_employee(employee1)
hr_department.add_employee(employee2)

engineering_department = Department("Engineering")
engineering_department.add_employee(employee3)

# Display employees in each department
hr_department.display_info()
engineering_department.display_info()