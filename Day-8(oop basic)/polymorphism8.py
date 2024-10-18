#poly --> many , multiple 
#morph --> shape

#polymorphism --> অনেকগুলো রকম 

class Animal :
    def __init__(self,name) -> None:
        self.name = name 
    
    def make_sound(self):
        print('Animal making sound')

class cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')
    
class dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('gheu gheu')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('vao vao')

don = cat('Real don')
don.make_sound()

shepard = dog('Local shepard')
shepard.make_sound()

messi = Goat('LM10')
messi.make_sound()

less = Goat('gora gori')

animals = [don, shepard , messi]

for animal in animals:
    animal.make_sound()
