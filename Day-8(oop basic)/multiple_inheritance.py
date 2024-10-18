class Family:
    def __init__(self,address) -> None:
        self.address = address

    
class school:
    def __init__(self,id , level  ) -> None:
        self.id = id
        self.level = level

class sport :
    def __init__(self  ,game) -> None:
        self.game = game 

class student(Family,school,sport):
    def __init__(self, address , id , level , game) -> None:
        school.__init__(self,id,level)
        sport.__init__(self,game)
        super().__init__(address)
        Family.__init__(self,address)