# 1,2,3,5,7,11
# logic - x>1 and x is divisible by 1 and x itself
#my method
number = int(input("Enter Number: "))
for i in range(2, number):
    if (number%i == 0):
        print("Not a prime")
        break
else: 
    print("Prime")

# 2nd Method
# prime=True
# for i in range (2,number):
#     if (number%i==0):
#         prime=False
#         break
# if prime:
#     print("Number is Prime")
# else:
#     print("Number is not Prime")