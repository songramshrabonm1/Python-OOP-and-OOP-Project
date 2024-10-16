# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/N

a, b = map(int , input().split())

s = input()


if(s[a] == '-'):
    have = True
    for i in range(0 , (a+b+1)):
        if i == a:
            continue
        elif s[i]>= '0' and s[i]<= '9':
            continue
        else:
            have = False
            break
    
    if have == True:
        print("Yes")
    else:
        print('No')
            
else:
    print("No")