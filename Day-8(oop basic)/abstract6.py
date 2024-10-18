from abc import ABC, abstractmethod
#abstract base class

class animal(ABC) :
    @abstractmethod #enforce all derived class to have a eat method 
    def eat(self):
        print('i need food')
    @abstractmethod
    def move(self):
        pass


class monkey(animal):
    def __init__(self , name) -> None:
        self.category = 'monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('hey i am eating banana')

    def move(self):
        print('hunging on the branches ')
        # return super().move()

lyka = monkey('lucky')
print(lyka.eat())


