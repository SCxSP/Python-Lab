numbers = list(map(int, input("Enter nos: ").split()))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)
