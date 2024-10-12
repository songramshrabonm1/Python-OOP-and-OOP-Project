print('Now i need Money ')
input()

input('Give Me some Money More : ')


money = input('Give Me Some Money: ')
print(type(money))

hello = input()
print(type(hello))
print("Here is your money variable value : ",money)

text = f"Here is your Money {money}"
print(text)


first_money = input('Krishna give me some Money : ')
second_money = input('Radha maa , please give some money ')
print('Money i Got from Krishna ',first_money,' And Radha maa ',second_money)
Total = first_money+second_money
#এটা String আকারে আসবে । 
print('Total Money I got , ', Total)


print('Type of first_money ',type(first_money))
print('Type of second_money ', type(second_money))


#আমরা যখন কোন একটা সংখ্যা input ণেই কোন user এর থেকে তখন এটা String এ আসে by default . 

first_money_int = int(first_money) # here type casting --> string to integer 
second_money_int = int(second_money)  # here type casting --> string to integer 
TotalGot = first_money_int+second_money_int
print('Total Money i Got : ', TotalGot)




num = 10 

print("Types of Variable before conversion : ",type(num))

converted_num = str(num)

print('After Conversion : ', converted_num)