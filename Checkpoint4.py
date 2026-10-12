class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.account_balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print("Withdrew:", amount)
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print("Balance:", self.account_balance)
        return self.account_balance

my_account = Account("123", 100, "Alice")

my_account.deposit(50)
my_account.withdraw(20)
my_account.check_balance()

second_account = Account("456", 50, "Bob")
second_account.withdraw(100)  
second_account.check_balance()
