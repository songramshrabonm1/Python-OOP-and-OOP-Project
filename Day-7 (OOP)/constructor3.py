class phone : 
    manufacture = 'china'

    def __init__(self , owner , brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
        # যদি আমরা কিছু না লিখি তাহলে আমাদের এখানে pass লিখতে হবে 

    def send_sms (self, phone , sms):
        text = f"sending to : {phone} {sms}"
        print(text)
        

my_phone = phone('kala chan', 'oppo', 23000)
print(my_phone.owner, my_phone.brand , my_phone.price)

Her_phone = phone('she amar jaan ', 'iphone', 30000)
print(Her_phone.owner, Her_phone.brand, Her_phone.price)


dad_phone = phone('abbu', 'Nokia', 3000)
print(dad_phone.brand,dad_phone.owner, dad_phone.price)