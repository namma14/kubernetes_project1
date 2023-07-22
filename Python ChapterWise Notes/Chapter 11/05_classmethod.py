'''Writing a prog to access/call attributes defined in class 
into a function defined'''
#1st method to use class method via dunder method (__class__).
class Employee:
    company="YouTube"
    Salary = 100000
    def changesalary(self,sal):
        self.__class__.Salary = sal #dunder method, this would get access to class attributes

e=Employee()
print(e.Salary)
e.changesalary(5000)
print(e.Salary)

# 2nd Method to use class method by defining class variable (cls) while defining function
# cls defined in function points to class defined
class Employee:
    company="YouTube"
    Salary = 90000
    @classmethod # need to define as it allows to define cls and access class attributes
    def changesalary(cls,sal):
        cls.Salary = sal #cls allows to access class attributes

e=Employee()
print(e.Salary)
e.changesalary(67000)
print(e.Salary)

