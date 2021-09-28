class User:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

christian = User("Christian Demesa", 2000)
bianca = User("Bianca Demesa", 4000)
james = User("James Demesa", 0)

christian.make_deposit(100)
christian.make_deposit(50)
christian.make_deposit(25)
christian.make_withdrawal(40)
christian.display_user_balance()

bianca.make_deposit(500)
bianca.make_deposit(1000)
bianca.make_withdrawal(50)
bianca.make_withdrawal(150)
bianca.display_user_balance()

james.make_deposit(100)
james.make_withdrawal(5)
james.make_withdrawal(20)
james.make_withdrawal(10)
james.display_user_balance()

christian.transfer_money(james, 50)
christian.display_user_balance()
james.display_user_balance()