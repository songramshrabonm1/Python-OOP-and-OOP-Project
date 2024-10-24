# read only --> you cant set the value . value cant be changed
#getter --> get a value of a property through a method. most of the time , you will get the value of private attribute
#setter --> set a value of a property through a method . most of the time you will set the value of a private property

class User:
    def __init__(self,name,age,money) -> None:
        self._name = name 
        self._age = age
        self.__money = money

    #getter without any setter is randomly attribute
    @property  # ei property lekhle tokhon ta r method thake na . eta tokhon hoye jay getter ar read only we can't set value this method 
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money
    
    #creat setter
    @salary.setter
    def salary(self,value):
        if value < 0 :
            return f"salary can not be negative"
        self.__money +=value


samsu = User('kopa',21 , 12000)

# print(samsu.__money)
print('before: ',samsu.salary)
samsu.salary = 4000
print('After: ',samsu.salary)