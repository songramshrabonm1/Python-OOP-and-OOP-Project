n = int(input())

fib = [0,1]

for i in range(2,50):
    fib.append(fib[i-1] + fib[i-2])


print(fib[n-1])


# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/O