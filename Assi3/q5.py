nums = list(map(int, input("Enter nos: ").split()))
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]
print("Evens:", evens)
print("Odds:", odds)
