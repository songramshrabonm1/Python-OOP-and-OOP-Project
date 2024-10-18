"""
Python Week 2 Practice Day 01

Create a Product class and a Shop class.
Inside the Shop class, create a method name add_product which adds products using the Product class to the Shop class.
Inside the Shop class, create a method name buy_product which is used to buy a product and check whether this product is available or not. If you successfully buy a product, then throw a Congress message.
What is Inheritance? Explain with examples
What are Encapsulation and Access Modifiers? Explain with examples

"""

class Product:
    def __init__(self,name,id,quantity, price) -> None:
        self.name = name
        self.id = id 
        self.quantity = quantity
        self.price = price

    # def __repr__(self):
        # self.productDetails = {self.name, self.quantity, self.price}
        # return self.name 
        # return f'product:{self.name} quantity:{self.quantity} price:{self.price}'
        # return {
        #     self.name,
        #     self.quantity,
        #     self.price
        # }
        # return self.__dict__
    def to_dict(self):
        return self.__dict__
    


class shop(Product):
    def __init__(self,name) -> None:
        self.productList = []
        self.name = name

        
    def add_product(self,name ,id, quantity , price):
        product = Product(name,id,quantity,price)
        self.productList.append(product.__dict__)

    def productListItem(self):
        for items in self.productList:
            print(type(items['quantity']))
        
    def buy_product(self,item_name):
        for  item in self.productList:
            if item['name'] == item_name:
                print(f'You can buy this product {item_name}')
                try:

                    Quantity = int(input('How many quantity  you want to buy : '))
                    if Quantity <= item['quantity'] :
                        return f"Congrats! You successfully bought {Quantity} {item_name}(s)."
                    else:
                        return f"Sorry, we don't have enough {item_name}. Available quantity: {item['quantity']}"
                except ValueError:
                    return "Invalid input. Please enter a valid number."


            # else:

            #     
        return f"Sorry, {item_name} is not available in the shop."
        


    

modir = shop('Songram Modir dokan')
modir.add_product('chal',2345,2,100)
modir.add_product('gom',2346,3,10)
modir.add_product('chini',2341,5,100)

# modir.productList()

# print(modir.productList)
result = modir.buy_product('chal')
print(result)
print(modir.buy_product('chini'))



# pp = Product('chini',23,3,1)
# productList = []
# productList.append(pp.__dict__)
# qq = Product('chal' , 23,5,1)
# productList.append(qq.__dict__)
# ss = Product('Dal',23,5,1)
# productList.append(ss.__dict__)


# print(productList)
# print(pp)
# print(qq)
# print(ss)