doubled = lambda num : num*num

number = [12, 56 , 98 , 78 , 56 , 12, 6 , 98 ]
doubles_num = map(doubled, number)
print(doubles_num) # Eta যদি চালাই আমাদের কে map object return করবে। 
# এখন আমরা যদি এটাকে লিস্ট এ কনভার্ট করে চলাই তখন এটা প্রিন্ট হবে লিস্ট আকারে 
print('numbers:  ', number)

print('doubles number: ',list(doubles_num))

squareNumber = map(lambda x : x*x , number)
print('Square Number : ',list(squareNumber))



actors = [
    {'name': 'sabana',
     'age' : 68
     },
    {'name': 'sabnur',
     'age' : 48
     },
    {'name': 'sabila',
     'age' : 30
     },
    {'name': 'sohana',
     'age' : 60
     },
    {'name': 'shrabonti',
     'age' : 35
     },
    {'name': 'koyel',
     'age' : 32
     }
]

juniors = filter(lambda actors : actors['age'] <40 , actors) # map পুরো টার  মধ্যে চলে আর filter টা  শুধু কন্ডিনশন এর উপর চলে  

print('junior actors : ',list(juniors))# map object return করবে তাই এখানে আমি এটা লিস্ট এ কনভার্ট করে প্রিন্ট করে দিচ্ছি 
