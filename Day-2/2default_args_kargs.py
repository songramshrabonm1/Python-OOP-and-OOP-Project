def sum(num1 , num2 ): 
    result = num1 + num2
    return result

total = sum(99, 11)# by default যত গুলো parameter  থাকবে ততগুলো argument  দিতে হবে  । 

print('Total : ',total)


def Sum (num1 , num2 , num3 = 5):
    result = num1+num2+num3
    return result

Total = Sum(1,2,3)
print('Total : ', Total)




#args 
def all_sum(*numbers):# এটা one kind of array এর মত কাজ করবে । 
    print(numbers)
    for num in numbers:
        print(num)

Tottal = all_sum(2,3) # এখন আমরা যতও খুশি তত দিতে পারবো  
print('print all_sum: ', total)



def all_sum(num1 , num2 , *Numberss ):
    print(Numberss)

    sum = 0 
    for nums in Numberss:
        print(nums)
        sum+= nums

    return sum


print(all_sum(4,3,23,5,1,9,52))



def do_a_lot(*args):
    print(args)
    return args


print("this is a do_a_lot function ",do_a_lot(43,32))
