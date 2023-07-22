#  Method via function
def divi(num):
    if num%5 == 0:
        return True
    else:
        return False


# Method2 via lamda
divi2 = lambda num: num%5==0

list1=[223,34,56,555,65,90]
print(list(filter(divi,list1)))
print(list(filter(divi2,list1)))