def full_name(fstName , lstName):
    name = fstName +" " + lstName
    return name

name = full_name('songram ', 'krishna ')
print(name)


name = full_name(lstName='krishnaaa ', fstName= ' songram ') # python এ serial maintain না করলে চলবে । 
print(name)

print("\n\n\n\n")

# define famous_name (**kargs) key argument 

def famous_name (first , last , title , **addition):
    name = f'{title} {first} {last}'
    print(addition)

    print(addition['hello1'])

    for key , values in addition.items():
        print(key, ' ', values)

    return name

nammee = famous_name(first= 'Songram ' , last= 'Krishna ' , title='sorbeshwar'  , hello1 = 'Krishnaaa' , hello2 = 'Radhamadhav' , hello3 = 'MadanMohan')

print(nammee)




#return multiple things from a function  

def a_lot(num1 ,num2 ):
    sum = num1 + num2
    sub = num1 - num2
    rem = num1 % num1

    return sum , sub , rem 


everything = a_lot(23,53) # এটা tupple আকারে আসবে । 

print(everything)


# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=25, location="New York")
# # Output:
# # name: Alice
# # age: 25
# # location: New York
