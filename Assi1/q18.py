print("Enter 5 nos: ")
lis=[]
for i in range(5):
    lis.append(int(input()))
n=int(input("Enter a number to remove: "))
lis.pop(n)
print(lis)