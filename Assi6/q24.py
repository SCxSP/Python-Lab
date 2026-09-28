class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class Student(metaclass=MyMeta):
    pass

name = input("Enter student name: ")
print("Created Student object for:", name)
