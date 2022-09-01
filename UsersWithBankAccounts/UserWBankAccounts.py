from BankAccount import BankAccount

#imported BankAccount to use its logic (correct word?)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

#line 9 pulling from BankAccount import

    def make_deposit(self):
        self.account.deposit(100)
        return self

    def make_withdraw(self):
        self.account.withdraw(100)
        return self

john = User("John", "john@email.com")



print(john)
