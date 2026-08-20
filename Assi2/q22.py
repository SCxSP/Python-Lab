Marks = [[], [], []]
n = 1
for Mark in Marks:
    Mark.extend(map(int, input(f"Enter Marks of Student {n}: ").split()))
    n += 1
n = 1
for Mark in Marks:
    print(f"Student {n} Total Marks: {sum(Mark)}")
    n += 1