try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
