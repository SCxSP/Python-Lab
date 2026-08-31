marks = []
while len(marks) is not 10: 
    marks += list(map(int, input(f"Enter {10 - len(marks)} marks: ").split()))
print("Max:", max(marks))
print("Min:", min(marks))
print("Total:", sum(marks))
print("Avg:", sum(marks) / len(marks))
