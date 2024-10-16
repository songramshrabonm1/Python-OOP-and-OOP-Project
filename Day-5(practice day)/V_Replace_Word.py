s = input()

ss = []


i = 0 
while i <= len(s)-1:
    # print(i)
    if i+4 <= len(s):
        if s[i] == 'E' and s[i+1] =='G' and s[i+2] == 'Y' and s[i+3] == 'P' and s[i+4] == 'T' :
            ss.append(' ')
            i+=5
            continue
        
    ss.append(s[i])
    i+=1


for char in ss:
    print(char,end='')