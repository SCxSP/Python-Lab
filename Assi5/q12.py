def is_even(n):
    return n % 2 == 0

n = int(input("Enter no: "))
print("Even" if is_even(n) else "Odd")
