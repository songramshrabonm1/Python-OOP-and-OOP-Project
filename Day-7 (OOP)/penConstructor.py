"""
1. calculator class to do add , deduct , multiply , divide
2. pen class . create three object with different instace attribute 


"""

class pen:
    
    def __init__(self, owner , brand , color ) :
        self.owner = owner
        self.brand = brand
        self.color = color


    def purpose(self, text):
        return f"amar kaj holo : {text}"


my_pen = pen('songram ', 'matador', 'black')
print(my_pen.brand,my_pen.color,my_pen.owner)

krishna_pen = pen('krishna', 'Nataraj','blue')
print(krishna_pen.brand,krishna_pen.owner,krishna_pen.color)
