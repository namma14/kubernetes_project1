# the key and corresponding value can be retrieved at the same time using the items() method.
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
print(knights.items())
# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for k, v in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(k, v))

# dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
z={x: x**2 for x in (2, 4, 6)} # creating 
print(z)