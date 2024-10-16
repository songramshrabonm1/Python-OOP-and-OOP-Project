# https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/K
n1 = int(input())
values = list(map(int , input()))

# print(values)

sum = 0 
for num in values:
    sum+=num

print(sum)