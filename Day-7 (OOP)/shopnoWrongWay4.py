class shop:
    cart = [] # এটা হয়ে গেলো ক্লাস Attribute এখানে আমরা যা ইন্সটেস্ন বানাবো এবং ওই ইন্সটেন্সের যেগুলো আমরা item add করবো সেগুলো সবগুলো instance এর টাই add হয়ে যাবে 
    # cart is a class attribute 
    
    def __init__(self,buyer) :
        self.buyer = buyer

    def add_to_cart(self , item):
        self.cart.append(item)




Krishna = shop('Krishna ')
Krishna.add_to_cart('flower')
Krishna.add_to_cart('phone')
print(Krishna.cart)


radhaMaa = shop('Radha')
radhaMaa.add_to_cart('jwelery')
print(radhaMaa.cart)

# now go to instace_att4.py 