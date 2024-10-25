class Vehicle:
    def __init__(self,brand,model) -> None:
        self.brand = brand 
        self.model = model
    def __repr__(self) -> str:
        return f"{self.brand}{self.model}"

class Car(Vehicle) :
    def __init__(self, brand, model , capacity) -> None:
        super().__init__(brand,model)
        self.milage = capacity
    
    def __repr__(self) -> str:
        return super().__repr__()
    
class Bike(Vehicle):
    def __init__(self, brand, model, milage) -> None:
        super().__init__(brand, model)
        self.milage = milage

    def __repr__(self) -> str:
        return super().__repr__()

toyotal = Car("Toyota", "corolla",4)
print(toyotal)
