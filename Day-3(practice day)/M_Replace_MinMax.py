n1 = int(input())

mylist = list(map(int, input().split()))



maximum = max(mylist)
minimum = min(mylist)

# print('maximum : ', maximum, ' minimum : ', minimum)

maximumIndex = mylist.index(maximum)
minimumIndex = mylist.index(minimum)


# print('maximum Index : ', maximumIndex, 'minimumIndex : ', minimumIndex)


mylist[maximumIndex] = minimum
mylist[minimumIndex] = maximum

# print(mylist)


for num in mylist:
    print(num , end=" ")
