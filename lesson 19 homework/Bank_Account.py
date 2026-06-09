class BankAccount:
    def __init__(self, owner_name: str, balance: int):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount

    @staticmethod
    def is_valid_amount(amount: int):
        return amount > 0