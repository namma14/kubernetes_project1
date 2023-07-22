# writnig a prog to understand different errors
try:
        number = int(input("Enter your number: "))
        Output = 1/number
        print(Output)
except ValueError as VE: # this would handle any error where expected input value is not provided
    print("Value Error Exception has occurred")
    print("Error: ",VE)

except ZeroDivisionError as ZDE: # this would handle only specific error where we are dividing a number by "0"
    print("Zero Division Error has occurred")
    print("Error: ",ZDE)
except Exception as e: # this exception would handle anykind of error.
     print("Any other code errors occoured: ")
     print("Error: ",e)