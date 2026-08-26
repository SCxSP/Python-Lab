age = int(input("Enter age: "))
if age < 12:
    cat, price = "Child", 100
elif age < 60:
    cat, price = "Adult", 200
else:
    cat, price = "Senior", 150
print(f"Category: {cat}, Price: {price}")
