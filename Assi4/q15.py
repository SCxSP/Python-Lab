bank_tot = 0
for i in range(3):
    cust_tot = 0
    print(f"Customer {i+1}:")
    for j in range(3):
        cust_tot += float(input(f"  Deposit {j+1}: "))
    print(f"Customer {i+1} Total:", cust_tot)
    bank_tot += cust_tot
print("Overall Bank Total:", bank_tot)
