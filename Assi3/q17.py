inv = {}
n = int(input("Enter no of products: "))
for i in range(n):
    inv[input("Enter product: ")] = int(input("Enter qty: "))
print(inv)

inv[input("Add product: ")] = int(input("Qty: "))
inv[input("Update product: ")] = int(input("New qty: "))
inv.pop(input("Remove product: "), None)
print(inv)
