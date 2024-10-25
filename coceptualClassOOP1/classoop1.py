
class product:
    def __init__(self , name , price) -> None:
        self.name = name 
        self.price = price
        
    def __repr__(self) -> str:
        return f'product Name : {self.name}  product Price : {self.price}'



class shop:
    
    def __init__(self , name) -> None:
        self.name = name
        self.products = [] 
    
    def __repr__(self) -> str:
        return f'This is shop name is : {self.name}'
    
    def add_product(self, name , price):
        productt = product(name,price)
        self.products.append(productt)



shop1 = shop('Test shop')
shop1.add_product('iphone',50000)
shop1.add_product('macbook',100000)

print(shop1)
print(shop1.products)

shop2 = shop('Test shop 2')
shop2.add_product('Monitor', 20000)
shop2.add_product('keyboard',4000)

print(shop2)
print(shop2.products)