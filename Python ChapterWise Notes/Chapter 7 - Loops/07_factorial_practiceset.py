# to find factorial of a number
#  10 =     1,2,3,4,5,
fac=1
num = int(input("Enter the Number: "))
for i in range (1,num+1):
    fac = i * fac
print(f" The factorial of {num} is {fac}")
