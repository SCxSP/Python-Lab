try:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    op = input("Enter op (+, -, *, /): ")
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b)
    else:
        print("Unknown operator")
except ZeroDivisionError:
    print("Error: Division by zero")
except Exception as e:
    print("Runtime Error:", e)
