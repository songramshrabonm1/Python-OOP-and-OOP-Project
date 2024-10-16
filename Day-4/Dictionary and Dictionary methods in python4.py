persons = {'name : ': 'kala pakhi ', 'address : ': 'kaliapur' , 'age: ': 23, 'job: ': 'facebooker'}

# {key : value , key : value , key : value} --> structure


print(persons)
print('\n\n\n')
print(persons.keys())
print('\n\n\n')
print(persons.values())
print('\n\n\n')
print(persons['name : '])


# mutable 
persons['language: '] = 'python'
# modify 
persons['name : '] = 'Krishna '


print('After modifying and mutable in dictionaries ', persons)

del persons['age: ']

print('After delete : ',persons)


convert_list = list(persons)

print('converting list : ',convert_list)




# only key : 
for items in persons:
    print(items)


print('\n\n\n')
print('key value ')
for key , value in persons.items():
    print(key, value)