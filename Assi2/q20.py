name = input("Enter name: ")
m1, m2, m3 = map(int, input("Enter 3 marks: ").split())
tot = m1 + m2 + m3
print(f"Name: {name}, Total: {tot}, Avg: {tot/3:.2f}")
