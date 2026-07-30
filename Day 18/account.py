class account :
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount , "was debited.")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
            self.balance += amount
            print("Rs.", amount , "was credited.")
            print("Total balance =", self.get_balance())

    def get_balance(self):
         return self.balance


acc1 = account(100000, 275632)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(109)
acc1.credit(347)
