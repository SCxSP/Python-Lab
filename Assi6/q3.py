def sum_n(n):
    return 1 if n <= 1 else n + sum_n(n - 1)

n = int(input("Enter n: "))
print("Sum:", sum_n(n))
