''' writing a program to understand self functionality
Self is passed when we are calling function defined in class module.
Self takes the argument passed while calling the function. If we don't write self while
defining function then when we call function, the function expects a argument
and program throws error.
'''
class Empolyee:
    company = "Google"
    def EmpSalary(self,signature):
        print(f"Salary of Employee working in company {self.company} is {self.Salary} {signature}")

Klinkara = Empolyee()
Klinkara.Salary = 100000
Klinkara.EmpSalary("Thanks") # OR Employee.EmpSalary(KlinKara)
# Self Logic:
''' both statements means same,but second statement shows that while
calling a function an argument is passed to function and if we don't pass
self as fucntion while defining the function. Program will throw an error stating 
that argument is passed when no argument is expected  
TypeError: Empolyee.EmpSalary() takes 0 positional arguments but 1 was given '''

