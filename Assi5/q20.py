from functools import reduce

numbers = list(map(int, input("Enter nos: ").split()))
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)
