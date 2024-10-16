name1 = 'krishna manomohana '
name2 = "krishna"

# s = ['hello']
# s.append(' dgdd')

print('s: ',s)

#multiline String
name3 = """ 
    krishna manomohana
    number one 
"""
print(name3)


print(name1)
print(name2)
print(name3)

name4 = 'krishna\'s devotee' #escape 
print(name4)

#string sequence of character

for char in name1:
    print(char)

#list হলো mutable means changeable 


print(name1[0]) #index/position value print
print(name2[1:6]) # slice করা 
print(name2[::-1]) #reverse string 
print(name2[-3])


# name2[0] = 'r'  we can't do this মান  সেট করতে পারব না। 

if 'krishna' in name1:
    print('Exist')


# string method 
print('before using upper : ',name3)
print('After upper : ', name3.upper())





#endwith() mehtod তা use করা হয় .extension বের করার জন্য। ধরি আমার ফাইল টা .pdf / .jpg  কিনা তা বের করার জন্য। 
# https://www.geeksforgeeks.org/python-string-methods/
# https://www.programiz.com/python-programming/methods/string