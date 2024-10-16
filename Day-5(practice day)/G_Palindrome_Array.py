# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G

n = int(input())

values = list(map(int , input().split()))

# print(values)

i = 0 
back = len(values) - 1 


# print('back', back)

palindrome = True
while i<=back:
    if values[i] != values[back]:
        palindrome = False
        break
    i+=1 
    back-=1

if palindrome == True:
    print("YES\n")
else: 
    print("NO\n")