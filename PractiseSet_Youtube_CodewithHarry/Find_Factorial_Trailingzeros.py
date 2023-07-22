# write a prog to find factorial of a number and trailing zeros in a factorial
# we will be using a recursive prog
# 5 = 5*4*3*2*1
# n = n * n-1
def fact (n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

number = int(input("Enter Number: "))
print(f"Factorial for Number {number} is: {fact(number)}")

'''1st Method: we are dividing the factorial by 10 untill it gives 
reminder as 0 but this approach has problem once the factorial is 
higher then it will not last and program will throw errors'''
def trailingzeros():
    num=int(input("Enter Number: "))
    fac = fact(num)
    count =0
    while(fac%10 == 0):
        count += 1
        fac = fac/10
    return count
tz = trailingzeros()
print(tz)

# Method2: we need to find how many 5's exist in a factorial of any number

def trailzeros():
    num = int(input("Enter Number: "))
    count =0
    while(num>=5):
        num = num//5
        count += num
    return count
print(trailzeros())

# Method3: 
# 100! = 100//5 + 100//25 + 100//125
# we will return the function at occurance of 1st zero and total the count i.e divisor of number this will be your trailing zeros
# number//i (//) floor division provides a reminder of int olny i.e if any decimal value is to be occurred in reminder then it will round off to nearest value
# we are storing the divisor of number//i to get the trailing zeros  
def trailzero():
        number = int(input("Enter Number: "))
        i =5
        count=0
        while (number//i !=0):
             count += int(number/i)
             i=i*5
        return count

print("Trailing zeros form Method3 are:",trailzero())
             
            
