def student_details(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

n = input("Enter name: ")
a = int(input("Enter age: "))
c = input("Enter course: ")

student_details(age=a, course=c, name=n)
