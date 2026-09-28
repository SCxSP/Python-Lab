class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(self.name, self.roll_no, self.marks)

s1 = Student(input("Name 1: "), input("Roll 1: "), float(input("Marks 1: ")))
s2 = Student(input("Name 2: "), input("Roll 2: "), float(input("Marks 2: ")))
s3 = Student(input("Name 3: "), input("Roll 3: "), float(input("Marks 3: ")))

s1.display()
s2.display()
s3.display()
