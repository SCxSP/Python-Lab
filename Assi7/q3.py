class Employee:
    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee(input("Name 1: "), float(input("Salary 1: ")))
e2 = Employee(input("Name 2: "), float(input("Salary 2: ")))

print(e1.name, e1.salary, e1.company)
print(e2.name, e2.salary, e2.company)
