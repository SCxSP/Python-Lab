name = input("Enter name: ")
roll = input("Enter roll: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

with open("student.txt", "w") as f:
    f.write(f"Name: {name}\nRoll: {roll}\nCourse: {course}\nMarks: {marks}\n")

print("Saved to student.txt")
