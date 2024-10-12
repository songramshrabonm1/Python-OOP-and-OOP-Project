
#break , continue 

num = 1
while num<10 :
    print(num, " hello")
    if num == 5 : 
        break
    num +=1 


num1 = 1 
while num1<10 :
    if num1== 5:
        num1+=1 
        continue
    print(num1)
    num1+=1


num1 = 1 
while num1 < 10 :
    print(num1)

    if num1%2 == 0 : 
        num1+=1 
        continue

    num1+= 1 


numss = [1,23,35,41,53,68,76,80,99,100]
index = 0 
nn = len(numss)
print('nn: ',nn)

while index < nn : 
    print(numss[index])
    index+=1 


