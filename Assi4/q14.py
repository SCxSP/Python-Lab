count = 0
while True:
    name = input("Enter name: ")
    roll = input("Enter roll: ")
    count += 1
    more = input("Register another? (y/n): ").lower()
    if more != 'y':
        break
print("Total Registered:", count)
