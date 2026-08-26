store = {"apple": 50, "milk": 30, "bread": 40, "rice": 100}
cart = {}
subtotal = 0

print("Store:", store)
while True:
    item = input("Enter item (or 'checkout'): ").lower()
    if item == 'checkout':
        break
    if item in store:
        qty = int(input("Enter qty: "))
        cart[item] = cart.get(item, 0) + qty
        subtotal += store[item] * qty
    else:
        print("Item not in store")

if subtotal >= 5000:
    disc_rate = 0.20
elif subtotal >= 3000:
    disc_rate = 0.10
elif subtotal >= 1000:
    disc_rate = 0.05
else:
    disc_rate = 0.0

discount = subtotal * disc_rate
final_bill = subtotal - discount

print("Cart:", cart)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Bill:", final_bill)
