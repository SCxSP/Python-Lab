class BankAccount:
    def __init__(self, balance, rate):
        self.balance = balance
        self.rate = rate

    def __calculate_interest(self):
        return self.balance * (self.rate / 100)

    def show_interest(self):
        print("Interest:", self.__calculate_interest())

b = float(input("Enter balance: "))
r = float(input("Enter rate (%): "))
acc = BankAccount(b, r)
acc.show_interest()
