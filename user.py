class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

christian = User("Christian Demesa", 2000)
bianca = User("Bianca Demesa", 4000)
james = User("James Demesa", 0)

christian.make_deposit(100).make_deposit(50).make_deposit(25).make_withdrawal(40).display_user_balance()

bianca.make_deposit(500).make_deposit(1000).make_withdrawal(50).make_withdrawal(150).display_user_balance()

james.make_deposit(100).make_withdrawal(5).make_withdrawal(20).make_withdrawal(10).display_user_balance()

christian.transfer_money(james, 50).display_user_balance()
james.display_user_balance()