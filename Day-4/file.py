# .csv comma separated value 
# .txt text file 


# আমি যদি চাই কোন একটা ফাইলের মধ্যে একটা কিছু লিখার জন্য এবং 
# with open('message.txt' , 'w') as file : 'w' দিলে লিখবে 
#     file.write('I love you , python')

# with open('message.txt' , 'a') as file: # আর 'a' দিলে append হবে। 
#     file.write('i love you krishna')

# with open('message.txt' , 'r') as file:
#     text = file.read()
#     print(text)



    # Search python file 


# with open('messagess.txt' ,'w') as file : 
#     file.write('I love you krishna')


# with open('messagess.txt', 'a') as file :
#     file.write(' how are you ')


with open('messagess.txt', 'r') as file:
    text = file.read()
    print(text)