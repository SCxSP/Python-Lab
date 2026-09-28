class Employee:
    def __init__(self, name, emp_id, dept, salary):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Dept: {self.dept}, Salary: {self.salary}")

e = Employee(input("Name: "), input("ID: "), input("Dept: "), float(input("Salary: ")))
e.display()
