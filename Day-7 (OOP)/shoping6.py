class Shopping :
    def __init__(self , name ):
        self.name = name 
        self.cart = []

    def add_to_cart(self , item , price , quantity):
        product = {'item': item , 'price': price , 'quantity': quantity}
        self.cart.append(product)

    def remove_item(self , item):
        for index , items  in enumerate(self.cart):
            if items['item'] == item:
                self.cart.pop(index)
                break
        



    def checkOut(self , amount):
        total = 0 
        for items in self.cart:
            print(items)
            total += items['price'] * items['quantity']

        print('total : ', total)
        if amount < total : 
            print(f'please provide {total- amount} more')
        else:
            print(f'You back extra :  {amount - total} tk')



Songram  = Shopping('Songram')
Songram.add_to_cart('Flower' , 230 , 5)
Songram.add_to_cart('Misti ', 200 , 2)
Songram.add_to_cart('Chini' , 300, 2)

print(Songram.cart)

Songram.checkOut(600)

Songram.remove_item('Flower')
Songram.checkOut(20000)