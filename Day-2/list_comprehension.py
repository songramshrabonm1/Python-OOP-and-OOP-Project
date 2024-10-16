number = [45 , 87 , 96 , 88, 40 , 65  , 43 , 85 ,14 , 26 , 61, 17,70 ]
odds = []
for num in number:
    if num % 2 == 1 and num % 5 == 0: 
        odds.append(num)


print(odds)
# odd_num = [num for num in number if num % 2 == 1 if num % 5 == 0]
odd_num = [num for num in number if num % 2 == 1 if num % 5 == 0] #listed comprehension 
print(odd_num)

players = ['sakib ', 'mushfiq ', 'mustafiz']
age = [38, 38 , 33 ]

for player in players: 
    print('player: ',player)
    for ages in age :
        print('Ages: ', ages)
