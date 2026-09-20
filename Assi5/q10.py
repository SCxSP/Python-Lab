def employee_details(name, department, salary):
    print(f"Name: {name}, Dept: {department}, Salary: {salary}")

name = input("Enter name: ")
dept = input("Enter dept: ")
sal = float(input("Enter salary: "))

employee_details(name, dept, sal)
employee_details(department=dept, salary=sal, name=name)
employee_details(name, salary=sal, department=dept)
