class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("balance is negative")
        return self

keem = BankAccount(0.01, 1000)
kendrick = BankAccount(0.01, 100)

# BankAccount.display_bank_account()

keem.deposit(100).deposit(2000).deposit(50000).withdraw(2000).yield_interest().display_account_info()
kendrick.deposit(1000).deposit(3000).withdraw(3000).withdraw(500).withdraw(200).withdraw(200).yield_interest().display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
        self.amount = 0


    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount
    
    def account_balance(self):
        self.balance

    def display_user_balance(self):
        print(f"User: {self.name} \nBalance: ${self.balance}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.balance += amount
        self.display_user_balance()
        user.display_user_balance()


keem = User("Baby Keem", BankAccount(0.01, 3000))

keem.make_deposit(2500)
keem.make_deposit(200)
keem.make_deposit(50)
keem.make_withdrawal(2000)
keem.display_user_balance()

kungfu_kenny = User("Kendrick Lamar", "pgLang@codingdojo.com")

kungfu_kenny.make_deposit(500000)
kungfu_kenny.make_deposit(250000)
kungfu_kenny.make_withdrawal(5000)
kungfu_kenny.make_withdrawal(20000)
kungfu_kenny.display_user_balance()


jay = User("Shawn Corey Carter", "rocafella@codingdojo.com")

jay.make_deposit(100000000)
jay.make_withdrawal(250000)
jay.make_withdrawal(500000)
jay.make_withdrawal(100000)
jay.display_user_balance()

    #  BONUS --> TRANSFER FROM FIRST TO THIRD USER

keem.transfer_money(20000000, jay)
