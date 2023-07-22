# writing a complex program to overload + and * operators.

class complexnumbers:
    def __init__(self,a,b):
        self.a = a #real number
        self.b = b # imaginary number

    def __add__(self,num):
        addreal = self.a+num.a 
        addimg = self.b + num.b
        print(f"{addreal}+{addimg}i")
        return complexnumbers(self.a+ num.a, self.b+num.b)
    def __sub__(self,num):
        subreal = self.a - num.a 
        subimg = self.b - num.b
        print(f"{subreal}+{subimg}i")
        return complexnumbers(self.a+ num.a, self.b+num.b)
    
    def __mul__(self,num1):
        mulreal = (self.a*num1.a - self.b*num1.b)
        mulimg = (self.a*num1.b + self.b*num1.a)
        print(f"{mulreal}+{mulimg}i")
        return complexnumbers(mulreal,mulimg)

    def __str__(self):
        print(f"{self.a} + {self.b}i")

    
c1 = complexnumbers(3,2)
c2 = complexnumbers(1,7)
add = c1+c2
sub = c1-c2
mul = c1*c2
