# writing a prog without defining a global variable explicitly
a = 5 # global variable
def globe():
    a=10 # local variable
    print ("Value of Local a",a)

k=globe()
print ("Value of Global a",a)

# writing a prog to define global variables
a = 5 # global variable
def globe():
    global a # defined a global variable.this would allow to overwrite the vlaue of a
    print ("Value of 1st a",a) # value 5 of 'a' will be printed
    a = 10 #this would overwrite the vlaue of global variable a
    print ("Value of 2nd a",a) # value 10 of 'a' will be printed as the same has been updated by global variable

k=globe()
print ("Value of 3rd a",a) # value 10 of 'a' will be printed as the same has been updated by global variable

