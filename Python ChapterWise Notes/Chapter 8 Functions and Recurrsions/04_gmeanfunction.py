# logic: (a*b)/a+b - formula to calculate geometric mean
def geomean (a,b):
    return (a*b)/(a+b)

gmean= geomean(5,6)
print("Geometric mean is: ", gmean)

#2nd method, we define default values to a and b
def geomean1 (a1, b1=8): # if there are 2 arguments passed in def function, we can't pass (a1=1,b1) b1 will give error but we can pass(a1,b1=9) means 1st variable can only have value 
                         # if 2nd argument also has value else 2nd argument will give error but 2nd argument can have value with 1st argument as empty
    return (a1*b1)/(a1+b1)

gmean1= geomean1(5) 
print("Geometric mean is: ", gmean1)