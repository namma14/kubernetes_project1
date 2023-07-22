# Concepts of Multilevel Inheritance
class Person:
    country = "India"
    name = "Arun"

class Employee(Person):
    company = "Google"
    country = "Haryana"
    def getempdetails(self):
        empcode = 112
        print(f"Employee code for {self.name} is {empcode} ")

class Programmer(Employee):
    company = "YouTube"
    language = "Python"
    name="bahadur"
    def getempdetails(self):
        empcode = 223
        print(f"Employee code for {self.name} is {empcode} ")


p= Person()
e= Employee()
pr = Programmer()
print(pr.company)
''' We are calling company variable using object of child class programmer. 
Company vairble is defined in  Person and Employee class but 
company is called Employee class because the employee class is parent class for programmer class
if company is not defined in Employee then company will be called from Person class
Person is parent class to EMployee and employee is parent to programmer'''
e.getempdetails()
pr.getempdetails()

