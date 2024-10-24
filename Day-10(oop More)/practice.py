import math
import time
def timer(funcc):
    def inner(*args, **kargs):
        print("Timer Started ")
        start = time.time()  
        funcc(*args, **kargs)
        print("Timer Ended")
        end = time.time()  
        print(f'timer : {end-start}')

    return inner


@timer
def get_factorial(n):
    print(f'Factorial Started')
    fact = math.factorial(n)
    print(f'Factorial result : {fact}')
    
get_factorial(5)