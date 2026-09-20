from functools import reduce

n = int(input("Enter n (e.g. 10): "))
prod = reduce(lambda a, b: a * b, range(1, n + 1))
print("Product:", prod)
