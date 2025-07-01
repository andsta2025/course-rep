class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have money to deposit: {amount}")
        else:
            print("You mast have some money to deposit")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance")

    def get_balance(self):
        return self.balance
    
    def show_balance(self):
        print(f"Current balance: {self.balance}") 

account = BankAccount("Juozas", 1000)
account.show_balance()
account.deposit(400)
account.show_balance()
account.withdraw(250)
account.show_balance()
account.withdraw(1500)  # Attempt to withdraw more than the balance
account.show_balance()
account.deposit(-100)  # Attempt to deposit a negative amount
account.show_balance()