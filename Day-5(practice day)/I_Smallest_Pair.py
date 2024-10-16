t = int(input())

while t!= 0:
    n = int(input())
    minimum = float('inf')
    valuess = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1 ,n ):
            value = valuess[i]+valuess[j] + j - i 
            minimum = min(minimum, value)




    print(minimum)
    t-=1

    # https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/I