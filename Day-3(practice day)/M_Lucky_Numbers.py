n1,n2 = map(int, input().split())

value = []

while n1<=n2:
    have = True

    Digit = n1 

    while Digit!=0:
        digit = Digit % 10 

        if digit!= 4 and digit!= 7: 
            have = False
            break

        Digit = Digit // 10

    if have == True:
        value.append(n1)

    n1+=1

if len(value) == 0:
    print(-1)
else:
    for num in value:
        print(num , end = " ")



