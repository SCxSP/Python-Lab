orders = {}
for i in range(15):
    item = input(f"Student {i+1} order: ")
    orders[item] = orders.get(item, 0) + 1
print("Orders:", orders)
