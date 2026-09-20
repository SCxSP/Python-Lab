def student_result(name, marks1, marks2, marks3):
    tot = marks1 + marks2 + marks3
    perc = (tot / 300) * 100
    print(f"Name: {name}, Total: {tot}, Percentage: {perc:.2f}%")

name = input("Enter name: ")
m1, m2, m3 = map(float, input("Enter 3 marks: ").split())
student_result(name, m1, m2, m3)
