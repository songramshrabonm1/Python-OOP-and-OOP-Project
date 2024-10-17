class shop:
    shopping_mall = 'Jamuna'

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute 


    def add_to_cart(self , item):
        self.cart.append(item)

krishna = shop('Krishna ')
krishna.add_to_cart('dress')
krishna.add_to_cart('jwelery')
print('Krishna cart : ',krishna.cart)


radha = shop('Radha')
radha.add_to_cart('panjabi')
radha.add_to_cart('flower')
print('Radha maa cart : ',radha.cart)


Modumangal = shop('ModuMangal')
Modumangal.add_to_cart('Misti')
Modumangal.add_to_cart('Rosmalai')
Modumangal.add_to_cart('Payes')
print('ModhuMangal cart : ', Modumangal.cart)

