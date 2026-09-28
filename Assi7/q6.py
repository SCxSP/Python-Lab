class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll_no}, Course: {self.course}")

s = Student(input("Name: "), int(input("Age: ")), input("Roll: "), input("Course: "))
s.display()
