n = int(input("Enter no of students: "))
d = {}
for i in range(n):
    name = input("Enter name: ")
    d[name] = int(input("Enter marks: "))
top = max(d, key=d.get)
print("Top:", top, d[top])
