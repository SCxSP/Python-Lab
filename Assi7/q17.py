try:
    a = int(input("Enter integer a: "))
    b = int(input("Enter integer b: "))
    print("Result:", a / b)
except ValueError:
    print("Error: Invalid integer input")
except ZeroDivisionError:
    print("Error: Division by zero")
