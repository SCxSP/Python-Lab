bal = float(input("Enter balance: "))
amt = int(input("Enter withdrawal amt: "))
if amt % 100 != 0:
    print("Amount must be multiple of 100")
elif amt > bal:
    print("Insufficient balance")
else:
    bal -= amt
    print("Withdrawal successful, Balance:", bal)
