class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.amount = 0


    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def account_balance(self):
        self.account_balance

    def display_user_balance(self):
        print(f"User: {self.name} \nBalance: ${self.account_balance}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()


keem = User("Baby Keem", "babykeem@codingdojo.com")

keem.make_deposit(2500).make_deposit(200).make_deposit(50).make_withdrawal(2000).display_user_balance()

kungfu_kenny = User("Kendrick Lamar", "pgLang@codingdojo.com")

kungfu_kenny.make_deposit(500000).make_deposit(250000).make_withdrawal(5000).make_withdrawal(20000).kungfu_kenny.display_user_balance()


jay = User("Shawn Corey Carter", "rocafella@codingdojo.com")

jay.make_deposit(1000000000).make_withdrawal(250000).make_withdrawal(500000).make_withdrawal(100000).display_user_balance()

    #  BONUS --> TRANSFER FROM FIRST TO THIRD USER

keem.transfer_money(20000000, jay)