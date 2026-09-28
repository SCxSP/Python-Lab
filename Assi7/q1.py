class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll_no}, Marks: {self.marks}")

for i in range(3):
    s = Student(input(f"Name {i+1}: "), input(f"Roll {i+1}: "), float(input(f"Marks {i+1}: ")))
    s.display()
