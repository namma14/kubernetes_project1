
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    if a==0:
        print("Enter Numerator value other than 0")
        exit()
    output=a/b
    print("Value of division is: ",output)
except ZeroDivisionError:
    print("Output of value divided by '0' is: Infinite")
    print("Enter value other than 0")