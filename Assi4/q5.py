p = float(input("Enter percentage: "))
if p >= 90:
    g, s = "A+", "Pass"
elif p >= 75:
    g, s = "A", "Pass"
elif p >= 60:
    g, s = "B", "Pass"
elif p >= 40:
    g, s = "C", "Pass"
else:
    g, s = "F", "Fail"
print(f"Grade: {g}, Status: {s}")
