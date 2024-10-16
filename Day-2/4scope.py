# #define global variable 
# balance = 3000 


# def buy_things(item, price):
# 		print('balance inside the function previous balance value : ',balance)
		
		 







# #global Variable --> 
# balance = 3000


# def buy_things(item, price):
#     dream_phone = 'xphone '

#     balancee = balance 
#     # global balance
#     print('balance inside the function previous balance value : ',balancee)
#     balancee -= 20
#     print(f'balance after buying {item} ' , balancee)



# buy_things('sunglass ', 1000 )



#global Variable --> 
balance = 3000


def buy_things(item, price):
    dream_phone = 'xphone '

    global balance
    print('balance inside the function previous balance value : ',balance)
    balance -= 20
    print(f'balance after buying {item} ' , balance)



buy_things('sunglass ', 1000 )
print( 'After using this variable into the buy_things function :  ' , balance)