# f7 = 0,1,1,2,3,5,8
num =7
n1=0
n2=1
sum=0
for i in range (num):
    print(sum,)
    n1=n2
    print ("n1:" ,n1)
    n2=sum
    print("n2: ",n2)
    sum=n1+n2
    print("sum: ",sum)

# 2nd method using recursion
def fabio(n):
    if n<=1:
        return n
    else: 
        return (fabio(n-1) + fabio(n-2))
    
num = int(input("Enter Number: "))
if num<=0:
    print("Enter a number greater than 0")
else:
    for i in range (num):
        print(fabio(i))