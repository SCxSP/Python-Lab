lis = list(map(int, input("Enter nos: ").split()))
n = int(input("Enter no to remove: "))
if n in lis:
    lis.remove(n)
print(lis)
