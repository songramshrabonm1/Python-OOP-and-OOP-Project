class Person:
    def __init__(self,name , age, height, weight) -> None:
        self.name = name 
        self.age = age 
        self.height = height 
        self.weight = weight 

    def exercise(self):
        raise NotImplementedError
    
    def eat():
        print(f'vat khaite lage moja')


class cricket(Person):

    def __init__(self, name, age, height, weight,team) -> None:
        super().__init__(name, age, height, weight)
        self.team = team

    #Override 
    def eat(self):
        print('Vegetable')

    def exercise(self):
        print('gym e jaw gam charao')

    # dander method --> + sign overload
    def __add__(self,other):
        return self.age + other.age

    # * sign operator overload
    def __mul__(self , other):
        return self.weight * other.weight
    
    # len overload
    def __len__(self):
        return self.height
    
    # > operator overload
    def __gt__(self , other): # greater than 
        return self.age > other.age
    
    def __le__(self, other): #less than
        return self.weight  > other.weight
    
    def __eq__(self,other) -> bool: #equal
        return self.weight == other.weight
    
    def __ne__(self,other):#not eqal
        return self.height != other.height
    
    def __lt__(self,other): #less than
        return self.age < other.age
    
    def __ge__(self,other):#greater than equal
        return self.height == other.height
    


shakib = cricket('shakib',36 , 5 , 58, 'Banglades')
mushfiq = cricket('mushfiq',37 , 5, 51 , 'Bangladesh')


print('Plus sign Operator Overload: ',53+98) # + sign operator overload
print([23,53] + [29,59,51,50,76])

print(shakib + mushfiq)
print(shakib * mushfiq)
print(len(shakib))
print(shakib > mushfiq) #compare 
print(shakib < mushfiq) #age compare it's give true because shakib age 36 and mushfiq age 37 
