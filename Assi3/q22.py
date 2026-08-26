n = int(input("Enter no of students: "))
d = {}
for i in range(n):
    d[input("Enter name: ")] = float(input("Enter marks: "))

for name, m in d.items():
    if m >= 75:
        res = "Distinction"
    elif m >= 60:
        res = "First Class"
    elif m >= 40:
        res = "Pass"
    else:
        res = "Fail"
    print(name, m, res)
