# # writing a program to develop a calculator which we can get sqaure, cube and squareroot
import math
class calculator:
    def square(self):
        num1 = int(input("Enter number to find Sqaure: "))
        square = num1**2
        print(f"Sqaure Root of {num1} is {square}")
    def cube(self):
        num2 = int(input("Enter number to find Cube: "))
        cube = num2**3
        print(f"Cube of {num2} is {cube}")
    def sqaureroot(self):
        num3 = int(input("Enter number to find Sqaure Root: "))
        sqaureroot = num3**0.5
        print(f"Sqaure Root of {num3} is {sqaureroot}") # without math module
        # print(f"Sqaure Root of {num3} is {math.sqrt(num3)}") # with math module
calc = calculator()
calc.square()
calc.cube()
calc.sqaureroot()

#2nd Method

class calc1:
    def __init__(self,number):
        self.num=number
    def square(self):
        print(f"Sqaure of {self.num} is {self.num **2}")
    def cube(self):
        print(f"Cobe of {self.num} is {self.num **3}")
    def squareroot(self):
        print(f"Sqaure Root of {self.num} is {self.num **0.5}")

calculation = calc1(9)
calculation.square()
calculation.cube()
calculation.squareroot()


