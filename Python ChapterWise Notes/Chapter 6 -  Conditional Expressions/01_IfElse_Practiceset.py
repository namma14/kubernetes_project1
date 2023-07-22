# writing a code to find grestest of 4 number
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 4th number: "))

# if n1>n2:
#     print("n1 is greater of 4 numbers")
# elif n2>n3:
#     print("n2 is greater of 4 numbers")
# elif n3>n4:
#     print("n3 is greater of 4 numbers")
# else:
#     print("n4 is greater of 4 numbers")

# 2nd method
if (n1>n4):
    f1=n1
else:
    f1=n4
if (n2>n3):
    f2=n2
else:
    f2=n3
if (f1>f2):
    print(f1, "is greatest")
else:
    print(f2,"is greatest")