from functools import reduce

numbers = [10, 20, 30, 40, 50]
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)
