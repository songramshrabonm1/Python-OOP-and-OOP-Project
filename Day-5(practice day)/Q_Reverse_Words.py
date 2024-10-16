# https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q
"""
here we can't take this input 
string = list(map(input().split()))

"""

string = list(input().split())
# print(string)

# for indexx in string:
#     print(indexx[::-1] , end=" ")



for I in range(0 , len(string)-1):
    # print(string[I])
    str = string[I]
    print(str[::-1] , end=" ")

# print(string[len(string) - 1])
lastIndex = string[len(string) - 1]
print(lastIndex[::-1])