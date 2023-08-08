'''
Bank class manages Account objects
'''
from Account import *

class Bank():
    def __init__(self):
        self.accounts_dict = {}
        self.account_number = 0

    def validate_account(self):
        '''Validate if accounts_dict contains users account number'''
        users_acc_num = input('Enter your account number ... ')
        try:
            users_acc_num = int(users_acc_num)
        except ValueError:
            raise AbortTransaction('The account number must be a valid number')
        if users_acc_num not in self.accounts_dict:
            raise AbortTransaction(f'There is no account {users_acc_num}')
        return users_acc_num

    def validate_password(self, account):
        passwd = input('Enter your password ... ')
        account.check_password(passwd)

    def get_users_account(self):
        '''Return the account matching the account number value'''
        users_acc_num = self.validate_account()
        the_account = self.accounts_dict[users_acc_num]
        self.validate_password(the_account)
        return the_account
    
    def create_account(self, user_name, initial_deposit, password):
        '''
        INPUT - user_name, initail deposit amount, a password
        OUTPUT - new account number added to accounts_dict
        '''
        new_account = Account(user_name, initial_deposit, password)
        new_account_number = self.account_number
        self.accounts_dict[new_account_number] = new_account
        self.account_number += 1
        return new_account_number
    
    def open_account(self):
        '''
        add an account to accounts_dict
        '''
        print('*** Open Account ***')
        user_name = input('Create username: ')
        user_password = input('Create password: ')
        starting_amount = int(input('Enter initial deposit: '))
        new_account = self.create_account(user_name,starting_amount,user_password)
        print(f'Your new account number is: {new_account}')
        self.account_number += 1
        print('\n')
    
    def close_account(self):
        '''
        remove an account from accounts_dict
        '''
        print('*** Close Account ***')
        self.validate_account()
        the_account = self.get_users_account()
        self.validate_password(the_account)
        the_balance = self.balance()
        print(f'Your balance of {the_balance} is being returned to you')
        del self.accounts_dict[account_number]
        print('Your account is now closed\n')
        
    def balance(self):
        '''
        print the current balance from Account
        '''
        print('*** Get Balance ***')
        the_account = self.get_users_account()
        the_balance = the_account.check_balance()
        print(f'Current balance is {the_balance}')
        
    def deposit(self, amount):
        '''Add money to account and print the new balance'''
        print('*** Deposit ***')
        the_account = self.get_users_account()
        the_balance = the_account.deposit(amount)
        print(f'Deposited {amount} into account')
        print(f'New balance is {the_balance}')

    def withdraw(self, amount):
        '''Remove money from account and print the new balance'''
        print('*** Withdraw ***')
        the_account = self.get_users_account()
        the_balance = the_account.withdraw(amount)
        print(f'Withdrew {amount} from account')
        print(f'New balance is {the_balance}')
        
    def print_test(self):
        print('Accounts Dashboard: ')
        for user_account in self.accounts_dict:
            the_account = self.accounts_dict[user_account]
            print(f'    Account number {user_account}')
            the_account.print_test()
        print('\n')

