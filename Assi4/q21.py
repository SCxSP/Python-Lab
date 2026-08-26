students = []
for i in range(8):
    students.append(input(f"Student {i+1} name: "))

for i in range(8):
    print(f"Seat {i+1}: {students[i]}")
