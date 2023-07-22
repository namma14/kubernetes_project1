# print a vector in 7i+8j+10k

class vect:
    def __init__(self,vec):
        self.vec = vec
    
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k "
            
v =vect([4,3,5])
print(v)

