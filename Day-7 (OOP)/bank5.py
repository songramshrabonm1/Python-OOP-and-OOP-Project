class Bank : 
    def __init__(self , bankName , balancee):
        self.bankName = bankName
        self.minWithdraw = 100
        self.maxWithdraw = 1000
        self.minOpenBankAmmount = 500
        self.balancee = balancee 
        

    

    def withdraw(self , amount):
        if amount < self.minWithdraw:
            print(f'you can\'t withdraw below {self.minWithdraw}')
        elif amount > self.maxWithdraw:
            print(f'You can\'t withdraw with more than {self.maxWithdraw}')
        else:
            print(f'your withdraw amount {amount}')
            print(f'before withdraw your total Balance : {self.balancee}')
            self.balancee -= amount
            print(f'After Withdraw Your balance : {self.balancee}')

    def deposite(self ,amount):
        if amount > 0 : 
            print(f'you deposite {amount} tk')
            print(f'Before deposite {amount} tk , Your balance : {self.balancee}')
            self.balancee += amount
            print(f'After deposite {amount} tk , Your balance : {self.balancee}')

    def get_balance(self):
        print(f'Your Balance : {self.balancee}')


songramAccount = Bank('Brac' , 150000)
songramAccount.deposite(200000)
songramAccount.get_balance()
songramAccount.withdraw(1000)
songramAccount.get_balance()


        

