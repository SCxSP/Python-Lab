marks = []
for i in range(3):
    m = list(map(int, input(f"Enter student {i+1} marks: ").split()))
    marks.append(m)

for i in range(3):
    print(f"Student {i+1} Total:", sum(marks[i]))