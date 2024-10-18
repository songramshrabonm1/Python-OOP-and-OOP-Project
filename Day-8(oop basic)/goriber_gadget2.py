class laptop : 
    def __init__(self , brand , price , color , memory) -> None:
        self.brand = brand 
        self.price = price 
        self.color = color 
        self.memory = memory

    def run(self):
        return f'Runing laptop {self.brand}'
    

    def coding (self):
        return f'learning python and practicing'
    
class phone : 
    def __init__(self , brand, price , color , dual_sim) -> None:
        self.brand = brand 
        self.price = price
        self.color = color
        self.dual_sim = dual_sim

    def run(self):
        return f'phone tipa tipi kore'
    def phone_call(self ,number, text):
        return f'sending sms to : {number} with :{text} '
    
class camera : 
    def __init__(self,brand , price ,color   , pixel ) -> None:
        self.brand = brand
        self.color = color
        self.price = price
        self.pixel = pixel
    def run(self):
        pass
    def change_lens(self):
        pass