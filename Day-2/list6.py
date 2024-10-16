#list , array in collection of same (simple terms )
#         0  1  2  3  4  5  6  7  8  9 
number = [45,56,12,89,87,32,89,59,46,93]
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


for num in number:
    print(num)

print( 'Number[3] : ',number[3])
print('number[-3]: ',number[-3])



#list(start : end) #start from the start index and stops before the end index 
print(number[2:6])
print(number[1:7]) # start from the 1 index and stop before the 7 index


#list(start:end:step)
print(number[1:7: 1])
print(number[1:6:2])
print(number[2:7:-1]) #এখানে কিছু পাওয়া যাবে না কারণ আমরা এখানে ২ থেকে উল্টো দিকে যাব আর উল্টো দিকে কোন ৭ ইনডেক্স খুঁজে পাব না। 
print(number[7:2:-1])

print(number[:5]) # এখানে প্রথম থেকে ৭ পরর্যন্ত চলবে। 
print(number[4:]) #এখানে ৪ নম্বর ইনডেক্স থেকে শেষ পরর্যন্ত চলবে 
print(number[:]) #এখানে সবগুলোই চলবে 
print(number[::-1])#উল্টো ভাবে চলবে। #shortcut to reverse a list 

