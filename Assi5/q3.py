def add_numbers(a, b):
    print("Sum:", a + b)
    print("Diff:", a - b)
    print("Prod:", a * b)
    print("Quot:", a / b if b != 0 else "Cannot divide by 0")

a = float(input("Enter first no: "))
b = float(input("Enter second no: "))
add_numbers(a, b)
