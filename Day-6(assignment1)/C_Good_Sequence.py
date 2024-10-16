n = int(input())


values = list(map(int , input().split()))

count_map = {}

for value in values:
    if value in count_map:
        count_map[value]+=1
    else:
        count_map[value] = 1 

remove = 0 
for key,value in count_map.items():

    countt = value
    if countt == key:
        continue
    elif countt > key:
        remove += (countt-key)
    else:
        remove += countt

print(remove)


# https://atcoder.jp/contests/arc087/tasks/arc087_a