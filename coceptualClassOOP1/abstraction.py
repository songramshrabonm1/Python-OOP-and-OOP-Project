from abc import ABC , abstractmethod
class Shape(ABC): # SHPAE KI KORE ABC CLASS KE INHERIT KORE TATE SHAPE CLASS ABSTRACT CLASS CREATE HOYE GELO . MANE TAR KHOMOTA ACHE ABSTRACT METHOD KE RAKHA 
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self , length , width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2*(self.length + self.width)
    
class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius
    
    def area(self):
        return 3.1416 * self.radius * self.radius
    
    def perimeter(self):
        return 2* 3.1416 * self.radius
    
    
rect = Rectangle(3,2)
print('Area: ', rect.area)
print('perimeter : ', rect.perimeter)
print('Rectangualr Area : ', rect.area)
print("Rectangular Perimeter : ",rect.perimeter)

circle = Circle(5)
print('Circle perimeter: ',circle.perimeter())
print('circle Area : ', circle.area())