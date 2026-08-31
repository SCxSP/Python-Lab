t = []
while len(t) is not 15: 
    t += list(map(int, input(f"Enter {15 - len(t)} Nos: ").split()))

t = tuple(map(int, input("Enter 15 nos: ").split()))
n = int(input("Enter no to search: "))
print("Found" if n in t else "Not found")
