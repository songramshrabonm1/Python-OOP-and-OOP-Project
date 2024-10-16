# list --> []
# tupple --> ()
# set --> {}



# set : unique items collection 

#create list 
numbers = [12, 56 , 98 , 78 , 56 , 12 ,6 , 98 ]
print('This is the numbers list: ', numbers)

#create set 
numbers_set = set(numbers)
print('numbsers_set : ', numbers_set)
numbers_set.add(59)
print('numbsers_set : ', numbers_set)


if 9 in numbers_set:
    print('exist')
elif 98 in numbers_set:
    print('exist')
else:
    print('not exist ')


if 5 not in numbers_set:
    print('not exist\n')
else: 
    print('exist\n')


for items in numbers_set:
    print(items , end=" ")



print('\n\n\n\n')

a = {1,3,4,5,7}
b = {1,2,3,4,5}
print(a&b)
print(a|b)


# set এ আমরা ইনডেক্স দিয়ে change করতে  পারব না। কিন্তু সেট muttable 