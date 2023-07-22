# n = 5
# for i in range(n,0,-1):
#     print (i*" *")

def starpattern(n):
    for i in range(n,0,-1):
        print(i*" *")

num = int(input("Enter Number: "))
starpattern(num)