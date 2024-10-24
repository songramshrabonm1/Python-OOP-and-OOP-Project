import math 
import time
def timer(func):
    def inner(*args , **kwargs):
        print('Time started')
        start = time.time()
        # print(func)
        func(*args, **kwargs)
        print('Time ended')
        end = time.time ()

        print(f'total time taken :{end-start}')

    return inner


 # আমি যদি কোন একটা ফাংশন কে decorator হিসেবে ব্যবহার করতে চাই তাহলে এই যে নিচের get_factorial() function টা timer() function এ চলে যাবে । এটা হচ্ছে আসলে এভাবে কাজ করবে timer(get_factorial) 
@timer
def get_factorial(n):
    print('Factorial Starting')
    result = math.factorial(n)
    print(f'factorial of {n} is : {result}')


get_factorial(55)
# timer()()
