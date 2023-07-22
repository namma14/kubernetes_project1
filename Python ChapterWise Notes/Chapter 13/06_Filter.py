# writing a prog for Filter Method
# syntax: list(filter(function,list)). This Method only takes iterable objects i.e list,tuple
# Method 1: filter method with defined function
def grt(num):
    if num > 5:
        return True
    else:
        return False


l1 = [2, 3, 4, 5, 6, 67, 7]
print(list(filter(grt, l1)))

# Method 2: filter method with Lamda function
grtr = lambda x:x>6
print(list(filter(grtr,l1)))