n = int(input("Enter no of employees: "))
emp = {}
for i in range(n):
    emp[input("Enter name: ")] = float(input("Enter salary: "))
avg = sum(emp.values()) / len(emp)
print("Avg:", avg)
for name, sal in emp.items():
    if sal > avg:
        print(name, sal)

