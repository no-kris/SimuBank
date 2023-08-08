'''
Main_Bank_Version_0.0.1
'''
from Bank import *

a_bank = Bank()

# Test accounts
johns_account = a_bank.create_account('John', 200, 'IloveYou123')
ashleys_account = a_bank.create_account('Ashley', 1200, 'RedPotato')

print('*** WELCOME TO BANK PROGRAM ***')

while True:
    print('\n')
    print('Press b to view account balance')
    print('Press c to close account')
    print('Press o to open an account')
    print('Press d to make a deposit')
    print('Press w to make a withdraw')
    print('Press s to view accounts dashboard')
    print('Press q to quit')
    print('\n')
    action = input('Make your choice ... ').lower()
    action = action[0]
    print('\n')
    try:
        match action:
            case 'b':
                a_bank.balance()
            case 'c':
                a_bank.close_account()
            case 'o':
                a_bank.open_account()
            case 'd':
                amount = input('Enter amount to deposit ... ')
                a_bank.deposit(amount)
            case 'w':
                amount = input('Enter amount to withdraw ... ')
                a_bank.withdraw(amount)
            case 's':
                a_bank.print_test()
            case 'q':
                break
            case _:
                print('That was not a valid option.\n')
    except AbortTransaction as error:
        print(error)
        print('Transaction Canceled')

print('Signing off, Adios')

            



