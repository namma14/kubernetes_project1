def greet(name="Stranger"): # we have passed a default value for name. if no value of name is passed then default value will be used
    print("Hello "+ name) 
greet()

# 2nd Method
def greet1(name1):
    k = "Hello " + name1
    return k # return will return the value to variable z for fucntion greet1
z= greet1("Nachiketa") # calling greet1 function, we have to provide the argument here else error will occur as we have not provided default value
print (z)