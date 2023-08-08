'''
class Account manages bank account operation such as deposit,
withdraw, check balance and create an account
'''

# Custom Exception
class AbortTransaction(Exception):
    '''exception to abort a bank transaction'''
    pass


class Account():
    '''
    name - the bank users name
    balance - the initial starting balance
    password - the bank users password
    '''
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = self.validate_amount(balance)
        self.password = password

    def validate_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction('Amount must be numerical')
        if amount <= 0:
            raise AbortTransaction('Amount must be a positive number')
        return amount
    
    def check_password(self, password):
        '''Match input password to self.password'''
        if password != self.password:
            raise AbortTransaction('Incorrect password')
    
    def deposit(self, amount):
        '''Insert specific amount into balance'''
        amount = self.validate_amount(amount)
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        '''Remove specific amount from balance'''
        amount = self.validate_amount(amount)
        if amount > self.balance:
            raise AbortTransaction('You cannot withdraw more than your current balance')
        self.balance -= amount
        return self.balance

    def check_balance(self):
        '''View the current balance'''
        return self.balance
    
    def print_test(self):
        print(f'    Name: {self.name}')
        print(f'    Balance: {self.balance}')
        print(f'    Password: {self.password}')
        print()