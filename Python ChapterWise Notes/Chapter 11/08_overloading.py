# writing a prog to understand overloading operators
class Number:
    def __init__(self,num):
        self.num = num
        print(num)
    
    def __add__(self,num1):
        print("Addition is: ", self.num + num1.num)
    
    def __mul__(self,num1):
        print("Multiplication is: ", self.num * num1.num)
    
    def __sub__(self,num3):
        print("Substraction is: ",self.num-num3.num)
    
    def __truediv__(self,num4):
        print("Division is: ",self.num/num4.num)
    
n = Number(8)
n1 =  Number(4)
n2 = Number (2)

add = n + n1
mul = n * n2
sub = n - n1
div = n/n2

