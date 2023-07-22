class Employee:
    company = "visa"
    level = 0

    def getLevel(self):
        self.level = self.level + 1

class Freelancer:
    company = "Fiverr"

class programmer(Employee,Freelancer): 
    '''#class programmer accesses method/attributes of parents class 
    in order of inheritance i.e Employee class is inherited first, 
    Employee class method/properties will be called first'''
    name = "Rohit"
    print(f"name is {name}")

p = programmer()
print(p.company) 
'''Company property is defined in both parent classes Employee and Freelance 
but company from Employee class will be printed in output as Employee 
class is inherited 1st by child class Programmer'''
p.getLevel()
print("Level of programmer is",p.level)