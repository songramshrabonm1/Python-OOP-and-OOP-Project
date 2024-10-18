#encapsulation : hide details 
#access modifier = public , private , protect
class Bank : 
    def __init__(self,Holder_name,initial_deposite ) -> None:
        self.Holder_name = Holder_name #public attribute
        self.__balance = initial_deposite #private attribute

    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self , amount):
        if amount < self.__balance:
            self.__balance-=self.__balance- amount
            return amount
        else:
            return f'fokira taka nai'


rafsan = Bank('Chutto bro',10000)

print(rafsan.Holder_name)
# print(rafsan.__balance)
print(dir(rafsan))
rafsan.deposite(40000)
print(rafsan.get_balance())