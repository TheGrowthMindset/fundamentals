# # class BankAccount:
#     # don't forget to add some default values for these parameters!
#     def __init__(self, int_rate, balance): 
#         # your code here! (remember, instance attributes go here)
#         # don't worry about user info here; we'll involve the User class soon
#     def deposit(self, amount):
#         # your code here
#     def withdraw(self, amount):
#         # your code here
#     def display_account_info(self):
#         # your code here
#     def yield_interest(self):
#         # your code here


class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

#         your code here! (remember, instance attributes go here)
#          don't worry about user info here; we'll involve the User class soon
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

keem = BankAccount(0.01, 100000000)
kendrick = BankAccount(0.05, 10)

# BankAccount.display_bank_account()

keem.deposit(100).deposit(2000).deposit(50000).withdraw(2000).yield_interest().display_account_info()
kendrick.deposit(1000).deposit(3000).withdraw(3000).withdraw(500).withdraw(200).withdraw(200).yield_interest().display_account_info()
