class Account:
    def __init__(self, accno, balance=0):
        self.balance = balance
        self.accno = accno

    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs",amount, "Debited from the account", self.accno, "Total Balance: ", self.balance)

    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs",amount, "Credited to the account", self.accno, "Total Balance: ", self.balance)

    def print_balance(self):
        print("Account No", self.accno, "Balance: ", self.balance)


s1 = Account(1234)
s1.print_balance()
s1.credit(50)
s1.debit(20)
s1.print_balance()