import sys

class bankApp:
    welcome='*******Welcome to the ATM*******'

    def __init__(self):
        self.Balance = 0
        self.calc()


    def withdraw(self, Amount):

        print(self.Balance)
        if self.Balance >= Amount:
            self.Balance -= Amount
            print("Current Balance: ", self.Balance)
            self.calc()
        else:
            print("insufficent")
            self.calc()

    def deposit(self, Amount):
        self.Balance += Amount
        print('current balance is', self.Balance)
        self.calc()

    def calc(self):
        print('Choose the transaction:')
        print('w as withdraw')
        print('d-deposit')
        print('e-exit')

        transaction = input('Transaction: w or d or e')
        if transaction == 'w' or transaction=='W':
            Amount = int(input('Enter the amount:'))
            self.withdraw(Amount)

        if transaction == 'd' or transaction =='D':
            Amount = int(input('Enter the amount to add in balance:'))
            self.deposit(Amount)

        elif transaction=='e' or transaction=='E':
            print("TQ for choosing US")
            sys.exit()
        else:
            print('choose valid transaction')
            self.calc()
bankApp()