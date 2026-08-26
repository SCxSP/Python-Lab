pin = "1234"
attempts = 0
while attempts < 3:
    p = input("Enter PIN: ")
    attempts += 1
    if p == pin:
        print("Access Granted")
        break
    print("Wrong PIN")
else:
    print("Account Locked")
