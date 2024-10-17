class Student:
    def __init__(self , name , currentClass , id):
        self.name    = name 
        self.id = id 
        self.currentClass = currentClass


    def __repr__(self) -> str: # আমরা যখন আমার অবজেক্ট টা কে প্রিন্ট দিবো তখন যাতে কিছু একটা দেখতে পারি তখন এটা use করবো 
        return f'Student with name {self.name} , class : {self.currentClass} , id: {self.id}'


class Teacher:
    def __init__(self , name , subject , id ) :
        self.name = name 
        self.subject = subject 
        self.id = id 

    def __repr__(self) -> str:
        return f'Teacher : {self.name} , subject : {self.subject} , id : {self.id}'
    

class school : 
    def __init__(self, name ) -> None:
        self.name = name 
        self.teachers = []
        self.students = []

    def add_teacher(self, name , subject) :
        id = len(self.teachers) + 101 
        teacher = Teacher(name , subject , id)
        self.teachers.append(teacher)

    def enroll(self , name , fee ):
        if fee < 6500 :
            return f'not enough fee'
        else:
            id = len(self.students) + 1 
            student = Student(name , fee ,id )
            self.students.append(student)
            return f'{name} is enrolled with id : {id} , extra money {fee - 6500}'


    def __repr__(self) -> str:
        print('Welcome To ', self.name)
        print('---------OUR TEACHERS----------')
        for teacher in self.teachers:
            print(teacher)
            # return f'{teacher}'
        print('----------OUR STUDENT-----------')
        for student in self.students:
            print(student)
            # return{student}
        return 'All done For now'



phitron = school('Phitron')
phitron.enroll('alia' , 5200)
phitron.enroll('Rani' , 8000)
phitron.enroll('Aisharya',9000)
phitron.enroll('vaijan',9000)

phitron.add_teacher('Tom Cruice','DS')
phitron.add_teacher('Krishna ', 'Algo')
phitron.add_teacher('Damodar', 'DATABASE')
print(phitron)