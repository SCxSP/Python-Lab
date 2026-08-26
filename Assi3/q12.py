t = tuple(map(int, input("Enter 15 nos: ").split()))
n = int(input("Enter no to search: "))
print("Found" if n in t else "Not found")
