# #  writing a program to add and multiply a vector of n dimensions
'''ai+bj and ci+dj
we will define the vector in form of list'''
class vec:
    def __init__(self,vector):
        self.vector = vector
        # print(vector)
    
    def __str__(self):
        vec1 = ""
        j=0
        for i in self.vector:
            vec1 += f"{i}a{j} +"
            j += 1
        return vec1 [:-1]
    
    def __add__(self,num):
        sum1=[]
        if len(self.vector) == len(num.vector):
            for i in range(len(self.vector)):
                sum1.append(self.vector[i] + num.vector[i])
            print("Sum of all items available in vector is",sum(sum1))
            return sum1
        else:
            print("Vectors are not same dimensional")
    def __mul__(self,num):
        # mul=[]
        mul1=0
        if len(self.vector) == len(num.vector):
            
            for i in range(len(self.vector)):
                # mul.append(self.vector[i] * num.vector[i])
                mul1 += self.vector[i] * num.vector[i]

            # print("Multiplicaiton of vectors is:", sum(mul))
            return mul1
        else:
            print("Both Vectors are not in same dimensions")
    def __len__(self):
        return len(self.vector)

v = vec([1,2,3,5])  
v1 = vec([5,7,8,7])
print("Sum of each Individual values available is",v+v1)
print("Multiplication of each Individual values available is",v*v1)
print(f"The vector is {len(v)} Dimensional")
# [1a0,2a1,3a2]


