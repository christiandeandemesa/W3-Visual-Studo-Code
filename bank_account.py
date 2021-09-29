class BankAccount:
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self
    def yield_interest(self, int_rate):
        if self.balance >= 0:
            self.balance *= int_rate
        return self
    @classmethod
    def display_inst(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "saving" : BankAccount(1.01, 2000),
            "checking" : BankAccount(1.03, 500)
        }
    def display_user_balance(self):
        print(f"User: {self.name}, Saving: {self.account['saving'].display_account_info()}")
        print(f"User: {self.name}, Checking: {self.account['checking'].display_account_info()}")
        return self
    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        return self

christian = User("christian")

christian.account['saving'].deposit(100).display_account_info()
christian.account['checking'].withdraw(100).display_account_info()
christian.display_user_balance()