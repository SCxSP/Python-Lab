n = int(input("Enter no of students: "))
students = []
for i in range(n):
    name = input("Enter name: ")
    m1, m2, m3 = map(int, input("Enter 3 marks: ").split())
    students.append([name, m1, m2, m3])
for s in students:
    print(s[0], sum(s[1:]))
