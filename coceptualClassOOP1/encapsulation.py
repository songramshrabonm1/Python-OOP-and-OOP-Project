class Product:
    def __init__(self,name , price) -> None:
        self.name = name 
        self.price = price
    def __repr__(self) -> str:
        return f"""
                   product name : {self.name} 
                   product Price : {self.price}
                """


class shop:
    def __init__(self , name ) -> None:
        """
        access modifier 3 types : private , protect , public
        _variable name (protected)
        __variable name (private)
        """
        self.name = name 
        self.__balance = 0 
        self.products = []
    def add_product(self,name , price):
        product = Product(name,price)
        self.products.append(product)
        self.__balance+=price 
    

    def getBalance(self):
        return self.__balance
    
    def __repr__(self) -> str:
        return f"shop name : {self.name}"
    
shop1 = shop('Arong')
shop1.add_product('chal', 2000)
shop1.add_product('dal',2000)
shop1.add_product('chini',3000)
print(shop1.products)
print(shop1.getBalance())
