n1, n2 = map(int, input().split())

values = list(map(int , input().split()))

for i in range(1, len(values)):
    values[i] = values[i-1] + values[i]

while n2 != 0:
    a, b = map(int, input().split())

    a -= 1
    b -= 1

    if a == 0:
        value = values[b]
        print(value)
    else:
        value = values[b] - values[a-1]
        print(value)

    n2 -= 1



# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y