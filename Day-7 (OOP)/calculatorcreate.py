class calculator : 
    brand= 'casio MS990'
    def add(self, num1,num2):
        return num1+num2
    def multiply(sef , num1 , num2):
        return num1*num2 
    def divide(self , num1 , num2):
        return num1 // num2
    def sub(self , num1 , num2):
        return num1-num2
    



my_calculator = calculator()

print(my_calculator)
print(my_calculator.brand)
print(my_calculator.add(2,3))
print(my_calculator.multiply(2,3))
print(my_calculator.divide(2,3))
print(my_calculator.sub(2,3))
