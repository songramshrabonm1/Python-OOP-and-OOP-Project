#define 
def double_it(num) : 
    result = num * 2 
    print(result)


double_it(5)
double_it(4)


def sum(num1 , num2 ):
    ssum = num1 + num2 
    return ssum

print(sum(4,2))
total = sum(5,10)
print('total value :' , total)


final= double_it(5)
print("Final double_it result : ", final ) # এখানে None আসবে কারণ আমরা এই ফাংশনে  কোন কিছু return করি নাই 


#আমরা যদি ফাংশন থেকে কোন কিছু মান পেতে চাই তখন return করতে হবে । 