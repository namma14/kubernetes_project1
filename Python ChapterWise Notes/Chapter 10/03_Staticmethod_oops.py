''' Sometimes we need to function that doesn't need a self object passed.
writing a program to under Static Method. Using static method
 we can define a function without defining self object for function.
'''
import datetime
class Empolyee:
    company = "Google"
    def EmpSalary(self,signature):
        print(f"Salary of Employee working in company {self.company} is {self.Salary} {signature}")
    @staticmethod # decorator to mark greet function as static method.
    def greet(): # no self object has been passed to greet function
        print("Welcome!!!")
    @staticmethod
    def time():
        print(datetime.date)

Klinkara = Empolyee()
Klinkara.Salary = 100000
Klinkara.EmpSalary("Thanks") # OR Employee.EmpSalary(KlinKara)
Klinkara.greet() # or Employee.greet(KlinKara).
Klinkara.time()
''' while calling greet function we are passing a object 
but since greet() function is defined via static method so python will ignore
the passed object while calling greet function'''