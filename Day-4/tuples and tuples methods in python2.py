def multiple():
    return 3,4 


print(multiple())
thingss = 'pen' , 'tripod' , 'water bottle'   , 'charger', 'phone ','web-cam'  , 'sunglass'
print(thingss)
print(type(thingss)) # check type 

print(thingss[0])
print(thingss[1])
print(thingss[-2])
print(thingss[3:6]) # slice 



print('\n')

if 'phone' in thingss:
    print('exist')


print('\n\n\n')

for item in thingss:
    print('item: ',item)

print('\n\n\n')

# things[0] = 'wagon' এটাও করা যাবে না কারণ String এর মতো Tupple ও চেঞ্জ করা যায় না 
print(thingss)


print('\n\n\n')


TupleSize = len(thingss) # check length
print('Item : ',TupleSize)

print('\n\n\n')

print('tupple inside the list : \n\n')

mega = ([2,3,4] , [6,8,9,5])
print('Type of mega tuple list : ',type(mega))
print(mega[0])
print('before change mega tupple : ', mega)
mega[0][1] = 6666 # আমরা Tupple কে আমরা পরিবর্তন করতে পারব না কিন্তু Tupple এর ভিতরে যদি muttable জিনিস থাকে তখন আমরা পরিবর্তন করতে পারব। এখানে tupple এর ভিতর list যা একটি muttable 
print('now mega tupple ', mega)


print('\n\n\n\n\n')


items = ('book ', 'monitor')
