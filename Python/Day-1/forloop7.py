# for(int i = 0 ; i<n;  i++){
    # int num = num[i];
#}



number = [5,10,15,20 , 25]
sum  = 0 
for num in number:
    print(num)
    sum+= num
    if sum > 20 : 
        print('Bigger Value ')


print(sum)


text = 'Pagla hawar tore '
for charf in text:
    print(charf)



#যদি নরমাল Traditional loop চালাতে চাই । 
#range(1,10) --> start টা হল inclusive আর last এর টা হল exclusive 
for i in range(1,10):
    print(i)


for i in range(5): #print 0 to 4 
    print(i)



#print also index value 
nums = [10,35,11,32,105,50,26]
for index , value in enumerate (nums ):
    print(f"index : {index} , value : {value}")



for index , value in enumerate(nums):
    print(f"index: {index}   values : {value}")