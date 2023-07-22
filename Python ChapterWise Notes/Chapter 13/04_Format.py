# writing a program for format function. It is used in earlier versions of python.
# it is replaced by f string.

#fstring
name = 'Nachiketa'
city = 'Palwal'
state = 'Haryana'
print("***Print string using f function****")
print(f"Programmers name is {name}, who belongs to city {city}\n")

# Format function
str1= "Programmers name is {}, who belongs to city {}" .format(name,city)
print("***Printing a string using format function***")
str2 = "Programmers name is {0}, who belongs to state {2} and city {1}" .format(name,city,state)
'''Format arguments can be provided by passing argument indexes in string variable
argument index starts with 0,1,2 etc. Values passed in argument gets as index value as they are passed
ex: 0 belongs to name, 1 belongs to city, 2 belongs to state'''
print(str1)
print(str2)
'''format function reads arguments in the order they are given and 
fill up the variable fields respectively'''