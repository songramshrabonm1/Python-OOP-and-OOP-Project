# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P
n = int(input())

value = list(map(int , input().split()))

minimum = float('inf')
cnt= 0 
while True:
    odd = False
    for index in range(len(value)):
        if value[index] % 2 == 0 and value[index] >0: 
            value[index] = value[index] /2 
            continue
        else:
            odd = True
            break

    

    if odd == True:
        break
    else: 
        cnt+=1 


print(cnt)
        


# while True:
    

# minimum = float('inf')
# for num in value:
#     cnt = 0 
#     if num %2 == 1 :
#         break
#     while num != 0 :
#         cnt+=1 
#         num = num // 2 
        
#         if num%2 == 1:
#             break
    
#     minimum = min(minimum,cnt)

# if minimum == float('inf') :
#     print(0)
# else:
#     print(minimum)