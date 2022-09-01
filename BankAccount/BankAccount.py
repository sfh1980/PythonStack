class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
    def yield_interest(self):
        (self.balance * self.int_rate) + self.balance
        return self


John_BankAccount = BankAccount(.02, 100)
John_BankAccount.deposit(50).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()

Jane_BankAccount = BankAccount(.02, 200)
Jane_BankAccount.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()