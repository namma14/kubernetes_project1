# logic: n! = n * (n-1)!
def calfactorial(number):
    if (number == 0 or number ==1):
        return 1
    else:
        return number * calfactorial(number-1)

number = int(input("Enter the number: "))
factorial = calfactorial(5)
print(f"Factorial of {number} is: ,{factorial}")