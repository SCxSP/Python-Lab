class BankAccount:
    def __init__(self, acc_no, balance):
        self.__account_no = acc_no
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance -= amt
        else:
            print("Insufficient funds")

    def display(self):
        print(f"Acc: {self.__account_no}, Balance: {self.__balance}")

acc = BankAccount(input("Acc no: "), float(input("Initial balance: ")))
acc.deposit(float(input("Deposit amt: ")))
acc.withdraw(float(input("Withdraw amt: ")))
acc.display()
