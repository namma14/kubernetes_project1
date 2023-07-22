# writing a prog to create class from another class using inheritance

class C2D:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    
    def print(self):
        return f"2-D Vector string is: {self.icap}i + {self.jcap}j"
        
class C3D(C2D):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap = k
    def __str__(self):
        return f"2-D Vector string is: {self.icap}i + {self.jcap}j + {self.kcap}k"
    
v2D = C2D (2,3)
v2D.print()
v3D = C3D (2,3,4)
# print(v2D)
print(v3D)
