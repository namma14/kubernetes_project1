# writing a prog for Finally with Try

try:
    number = int(input("Enter your number: "))
    z = 1/number
    print(z)

except ValueError as VE:
    print("Enter Integer values")
    exit() # quit the program

except ZeroDivisionError as ZDE:
    print("Enter integer except '0'")
    exit() # quit the program

finally: # this peice of code will get executed regardless whether try block is executed or except block is executed.
         # Finally block is executed even when exit function has also been called in except block.
    print("We are done")