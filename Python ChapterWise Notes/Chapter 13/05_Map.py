# maps is used when you want to apply a function to all items

# Method1, wirintg a prog to find sqaure of all values defined in list via for loop
l1=[2,3,5]
l2=[]
a=5
def square(sqr):
    return sqr*sqr
for i in l1:
    l2.append(square(i))
print(l2)

# Method2, wirintg a prog to find sqaure of all values defined in list via Map method
#syntax : map(function,argument/input_list 'In Input_list argument we can only pass iterable object')
print(list(map(square,l1))) # to print the output we need to type cast it into list

# Method2, wirintg a prog to find sqaure of all values defined in list via Map method and Lamda function
sqaure1 = lambda x:x*x # sqaure1 function is defined using lamda function
print(list(map(sqaure1,l1))) # map works with lamda function as well