#static attribute (class attribute)
#static method @staticmethod
#class method @classmethod
class Shopping:
    cart = []#class attribute # static attribute
    origin = 'china'

    def __init__(self ,name , location) -> None:
        self.name =name #instance attribute
        self.location = location

    def purchase(self,item,price,amount):
        remaining = amount - price
        print(f'Buying : {item} for price: {price} and Remaining : {remaining}')

    @classmethod
    def hudai_dekhi( cls,item):
        print(cls.origin)
        print('hudai dekhi kintu kinmu na jst ac er hawa khaite aschi',item)

    @staticmethod
    def multiply(a,b):
        return a*b
    
    """ 
        static method does not take specific parameter (ekahne self er element use korte dibe  na )

    """



bashudara = Shopping('basundara', 'not popular location')
bashudara.purchase('lungi',2,3)
bashudara.hudai_dekhi('lungii')

Shopping.purchase('a',2,3,4) # evabe jodi access korte chai tokhon amra self er jonno ekta item beshi dite hobe 
# Shopping.hudai_dekhi('lungi') # eta use korte partesi eivabe karon ami ekhane bole diyechi eta ekta class method 

#static method er somoy o amra evabe access korte pari . static method instance er jonno use kora hoy na 
print(Shopping.multiply(3,2))
# bashudara.multiply(7,9) amra evabe use korte jabo na static method 