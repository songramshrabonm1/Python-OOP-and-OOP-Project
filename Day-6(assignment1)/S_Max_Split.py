# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s


s = input()
cnt = 0 
l = 0 
r = 0 
rPrevious = False
tuple = ()

str = [] 

for i in range(0 , len(s)):

    if (l == r and (l>0 and r > 0 ))  :
        cnt+=1 
        # print('string : ',str,'\n\n')
        tuple = tuple + (list(str),)
        
        # print('after adding tupple : ',tuple,'\n\n')

        str.clear()
        # print('clearing : ', str,'\n\n')
        l = 0 
        r = 0 
        rPrevious = False
    

    if s[i] == 'L':
        l+=1 
        str.append('L')
        rPrevious = False
    else:
        r+=1 
        str.append('R')
        rPrevious = True
        


# print('while loop outside : ',tuple)
if len(str) > 0 : 
    tuple = tuple + (str,)
    cnt+=1


print(cnt)


for items in tuple:
    for valueess in range(0 , len(items)):
        print(items[valueess],end='')
    
    print()

# # We can iterate tupple string like this : 
# for items in tuple :
#     print(''.join(items)) # Join list of characters into a string
