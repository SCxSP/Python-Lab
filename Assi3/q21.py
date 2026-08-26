name = input("Enter name: ")
m = {
    "Math": float(input("Enter Math: ")),
    "Python": float(input("Enter Python: ")),
    "DBMS": float(input("Enter DBMS: ")),
    "CN": float(input("Enter CN: "))
}
tot = sum(m.values())
avg = tot / 4
if avg >= 90:
    g = "A+"
elif avg >= 80:
    g = "A"
elif avg >= 60:
    g = "B"
elif avg >= 40:
    g = "C"
else:
    g = "F"
print("Total:", tot, "Avg:", avg, "Grade:", g)
