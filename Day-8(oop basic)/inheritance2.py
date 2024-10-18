#based class , parent Class , common functionality + attribute 
#derived class , child class , uncommon attribute + functionality 

class Gadget:
    def __init__(self , brand , price , color, origin ):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running Laptop : {self.brand}'




class laptop : 
    def __init__(self , memory , Processor) -> None:
        self.memory = memory
        self.processor = Processor

   

    def coding (self):
        return f'learning python and practicing'
    
class phone(Gadget) : 
    def __init__(self ,brand, price ,color, origin ,dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,price,color ,origin)

    def run(self):
        return f'phone tipa tipi kore'
    def phone_call(self ,number, text):
        return f'sending sms to : {number} with :{text} '
    
    def __repr__(self) -> str:
        return f'Phone :{self.brand} {self.price} {self.dual_sim}'
    
class camera : 
    def __init__(self, pixel ) -> None:

        self.pixel = pixel


    def change_lens(self):
        pass


myphone = phone(Iphone , 120000, 'Silver', 'China',True)

print(myphone)
