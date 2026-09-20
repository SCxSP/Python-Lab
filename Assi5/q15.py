check_num = lambda x: "Positive" if x > 0 else ("Zero" if x == 0 else "Negative")

n = float(input("Enter no: "))
print("Result:", check_num(n))
