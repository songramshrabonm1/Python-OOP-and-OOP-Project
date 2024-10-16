#1
number = [12, 45 , 98 , 68 ]
number.append(23) # last এ add করবে । 
print(number)

#2
number.insert(2 , 71) # first index then add value . 
print(number)

number.insert(3,81)
print(number)

#3
number.remove(98) # কোন ভ্যালু কে রিমুভ করবো তা সরিয়ে দেয়ার জন্য আমরা এই ভ্যালু টা দিবো 
# যদি না থাকত তখন আমাকে error দিত x not in list 


#4 
last = number.pop() # last এর উপাদান টা  বের করে দিবে এবং তুমি চাইলে ভ্যারিয়েবল সেভ করতে পারবে 
print(last)


#5
index = number.index(71)
print(index)
# যদি না থাকত তখন দেখাত ৫ is not in the list 

# এটা আমরা যাতে error না খাই তাই আমাদের এভাবেও করতে পারি 
if 71 in number:
    index = number.index(71)
    print('5 index value : ',index)



#6
howMany = number.count(5) # একটা element কতবার আছে তা দেখার জন্য এটা use করব 
print('HowMany : ', howMany)


#7 
number.sort()
print(number)




#8
number.reverse()
print(number)