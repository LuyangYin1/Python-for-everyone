class BankAccount:
    def __init__(self, holder_name, account_number, balance=0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance
        print(
            f"Account Holder: {self.holder_name}, Account Number: {self.account_number}, Balance: ${self.balance}"
        )

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return f"Insufficient funds to remove ${amount}. Current balance: ${self.balance} or invalid withdrawal amount."

    def get_balance(self):
        return f"Current balance: ${self.balance}"

    def get_account_number(self):
        return f"Account number: {self.account_number}"

    def get_holder_name(self):
        return f"Account holder: {self.holder_name}"

    def __str__(self):
        return f"Account Holder: {self.holder_name}, Account Number: {self.account_number}, Balance: ${self.balance}"


class SavingsAccount(BankAccount):  # Inherits from BankAccount
    def __init__(self, holder_name, account_number, balance=0, interest_rate=0.01):
        super().__init__(
            holder_name, account_number, balance
        )  # Call parent's constructor
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Added interest of ${interest}. New balance: ${self.balance}"
