l1 = list(map(int, input("Enter list 1: ").split()))
l2 = list(map(int, input("Enter list 2: ").split()))
for a, b in zip(l1, l2):
    print(a + b)
