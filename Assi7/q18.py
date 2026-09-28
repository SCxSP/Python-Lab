try:
    n = int(input("Enter integer: "))
    res = n * n
except ValueError:
    print("Error: Not a valid integer")
else:
    print("Square:", res)
finally:
    print("Execution completed")
