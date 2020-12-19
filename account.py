class Account:

    def __init__(self, balance=0, limit=0):
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount
        print("Successfully deposited $" + str(amount) + ".")

    def withdraw(self, amount):
        if amount > self.limit:
            print("Amount to withdraw exceeds account limit.")
            return

        if self.balance - amount < 0:
            print("Cannot withdraw amount exceeding balance.")
        else:
            self.balance -= amount
            print("Successfully withdrew $" + str(amount) + ".")

    def read_balance(self):
        print("Your Balance: $" + str(self.balance))



