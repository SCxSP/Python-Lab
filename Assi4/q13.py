while True:
    print("1. Coffee\n2. Tea\n3. Hot Chocolate\n4. Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        print("Dispensing Coffee")
    elif ch == "2":
        print("Dispensing Tea")
    elif ch == "3":
        print("Dispensing Hot Chocolate")
    elif ch == "4":
        print("Exiting")
        break
    else:
        print("Invalid choice")
