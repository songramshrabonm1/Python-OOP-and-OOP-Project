class salary:
    def __init__(self,Salary,bonus) -> None:
        self.Salary = Salary 
        self.bonus = bonus 

    def annualSalary(self):
        return (self.Salary * 12 )+ self.bonus
    
class Employee : 
    def __init__(self , name , age,  Salary , bonus) -> None:
        self.name = name 
        self.age = age 
        self.ObjectSalary = salary(Salary, bonus)
    def Total_salaryy(self):
        return self.ObjectSalary.annualSalary()
    
    def __repr__(self) -> str:
        return f"""
                    Employee Name : {self.name}
                    Employee Age : {self.age}
                    Employee Salary : {self.Total_salaryy()}
                """

songram = Employee('Songram ', 23, 24000, 5000)
print(songram)
    