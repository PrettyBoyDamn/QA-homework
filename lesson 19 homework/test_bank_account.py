from Bank_Account import BankAccount

def test_deposit():
        account = BankAccount("John Doe", 100)
        account.deposit(50)
        assert account.balance == 150
    
def test_withdraw():
        account = BankAccount("John Doe", 100)
        account.withdraw(20)
        assert account.balance == 80

def test_static_function():
        result = BankAccount.is_valid_amount(-10)
        assert result == False