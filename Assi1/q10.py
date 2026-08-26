name = input("Enter name: ")
m1, m2, m3 = map(float, input("Enter 3 marks: ").split())
tot = m1 + m2 + m3
print("Name:", name)
print("Total:", tot)
print("Avg:", tot / 3)
