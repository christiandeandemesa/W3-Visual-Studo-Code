class BankAccount:
    all_accounts = []
    def __init__(self="Christian Demesa", int_rate=1.01, balance=2000): 
        self.name = self
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

christian = BankAccount()
bianca = BankAccount("Bianca Demesa")

christian.deposit(60).deposit(20).deposit(45).withdraw(20).yield_interest(1.01).display_account_info()
bianca.deposit(1000).deposit(1500).withdraw(100).withdraw(200).withdraw(50).withdraw(45).yield_interest(1.01).display_account_info()

BankAccount.display_inst()