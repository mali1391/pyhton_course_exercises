class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.acount_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            raise ValueError("deposit amount must be positive !!")

        self.balance += amount
        print(f"successfully deposited: {amount} !!")

    def withdraw(self, amount):
        if amount >= 0:
            raise ValueError("withdraw amount must be positive !!")

        self.balance -= amount
        print(f"successfully withdrawn: {amount} !!")

    def show_balance(self):
        print(f"current balance: {self.balance}")

def exhibit():
    account = BankAccount("123456789", 1000)

    try:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    except ValueError as e:
        print("Value Error:", e)

    except InsufficientBalanceError as e:
        print("Bank Error:", e)

    account.show_balance()

exhibit()