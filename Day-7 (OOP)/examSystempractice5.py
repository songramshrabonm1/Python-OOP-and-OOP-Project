"""
Exam attend to exam get marks 
"""


class exam():
    def __init__(self):
        self.Bangla  = False

        self.English  = False
 
        self.Math  = False


        self.result = {}
        self.TotalMarks = 0


    def Banglaaa(self,Banglaa , marks) :
        self.Bangla = Banglaa
        self.marks = marks
        self.result['Bangla'] = self.marks

    def banglaResult(self):
        marks = self.result['Bangla']
        self.TotalMarks += marks
        if marks>= 80 :
            print(f'congratualations , you got A+ in Bangla . your Marks: {marks} ')
        elif marks>=70:
            print(f'Congratulation , You got A in Bangla . you mark : {marks}')
        elif marks>=33:
            print(f'Congratulation You passed you Bangla Exam . your marks : {marks}')
        else:
            print(f'Sorry to say you failed Bangla Exma . Your marks : {marks}')

    
        


    def Englishh(self,Englishh , marks) :
        self.English = Englishh
        self.marks = marks
        self.result['English'] = self.marks
        
    
    def EnglishResult(self):
        marks = self.result['English']
        self.TotalMarks += marks

        if marks >= 80 :
            print(f'congratualations , you got A+ in English . your Marks: {marks} ')
        elif marks >= 70:
            print(f'Congratulation , You got A in Englis . you mark : {marks}')
        elif marks >= 33:
            print(f'Congratulation You passed you English Exam . your marks : {marks}')
        else:
            print(f'Sorry to say you failed English Exma . Your marks : {marks}')
        
    
    def Mathh(self,Mathh , marks) :
        self.Math = Mathh
        self.marks = marks
        self.result['Math'] = self.marks
        

    def MathResult(self):
        marks = self.result['Math']
        self.TotalMarks += marks
        if marks>=80:
            print(f'Congratulations , you got A+ in Math , Your marks : {marks}')
        elif marks>= 70 :
            print(f'Congratulation you got A in Math exam , Your marks : {marks}')
        elif marks >= 33:
            print(f'Congratulation You passed you Math Exam . your marks : {marks}')
        else:
           print(f'Sorry to say you failed English Exma . Your marks : {marks}')

    def fullResult(self):
        for key , values in self.result.items():
            if values < 33 :
                print(f'{key} : Failed')
            else:
                print(f'{key} : {values}')

            


    def TotalMarkss(self):
        if self.Bangla == True and self.Math == True and self.English == True :
            print(f'Your TotalMarks : {self.TotalMarks}')
        else:
            print(f'You failed Your exam ')



ShrabonExam = exam()


bangla = input('Bangla Exam Attend? ')
bangla = bangla.upper()
print(bangla)
if bangla == 'YES':
    BanglaMarks = int(input('Enter Marks Bangla Exam : '))
    ShrabonExam.Banglaaa(True,BanglaMarks)
else:
    ShrabonExam.Banglaaa(False, 0)


eng = input('English Exam Attend ? ')
eng =  eng.upper()
if eng == 'YES':
    EnglishMarks = int(input('Enter Marks English exam : '))
    ShrabonExam.Englishh(True , EnglishMarks)
else:
    ShrabonExam.Englishh(False, 0)
    
mat = input('Math Exam attend? ')
mat =  mat.upper()

if mat == 'YES':
    mathresult = int(input('Enter the Math Marks : '))
    ShrabonExam.Mathh(True, mathresult)
else:
    ShrabonExam.Mathh(False,0)

        

ShrabonExam.banglaResult()
ShrabonExam.MathResult()
ShrabonExam.EnglishResult()

ShrabonExam.TotalMarkss()
ShrabonExam.fullResult()

    
      