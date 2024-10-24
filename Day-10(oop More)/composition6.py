class cpu:
    def __init__(self,cores) -> None:
        self.cores = cores
    def __repr__(self) -> str:
        return f'{self.cores}'
    
class ram :
    def __init__(self , size) -> None:
        self.size = size

    def __repr__(self) -> str:
        return f'{self.size}'

class HardDrive : 
    def __init__(self , capacity) -> None:
        self.capacity = capacity

    def __repr__(self) -> str:
        return f'{self.capacity}'

#computer has a cpu
#computer has a ram 
#computer has a harddisc
class computer:
    def __init__(self,name, cores, sizes , capacity) -> None:
        self.cpu = cpu(cores)
        self.ramSize = ram(sizes)
        self.Hard_disc = HardDrive(capacity)
        self.name = name 

    def __repr__(self) -> str:
        return f"""
                    Computer Name : {self.name} 
                    Computer Ram Sizes : {self.ramSize}
                    Computer Cpu cores : {self.cpu}
                    Computer HardDisc : {self.Hard_disc}
                """

mac = computer('Macbook',8,8,256)
print(mac)

