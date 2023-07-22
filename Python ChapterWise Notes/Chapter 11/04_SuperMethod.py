# Concepts of Multilevel Inheritance
class Person:
    country = "India"
    name = "Arun"

    def __init__(self):
        print("Intializing Person ....")


    def getempdetails(self):
        empcode = 400
        print(f"Employee code for {self.name} is {empcode} ")

class Employee(Person):
    company = "Google"
    country = "Haryana"
    language = "C++"
    
    def __init__(self):
        super().__init__()
        print("Intializing Employee ....")
    
    def getempdetails(self):
        name="vijay"
        empcode = 200
        print(f"Employee code for {name} is {empcode} and company is {self.company} & language {self.language}")
''' getempdetails() function ko humne programmer class me super function ki help se
call kia lekin apne ko sabhi variable function ke ander hi declare kare padenge agar wo
sab ko print karna h to varna programmer class ke similar variables ki values 
employee class k variable ko overwrite kar deta h
Ex: name and empcode dono class me common h, ye variable agar function k bahar class me define kare 
aur super function call kia programmer class se to variable overwrite ho jayenge
isliye variable ko function k andar declare karo taki to overwrite na ho'''
class Programmer(Employee):
    company = "YouTube"
    language = "Python"

    def __init__(self):
        super().__init__()
        print("Intializing Programmer ....")
    
    def getempdetails(self):
        super().getempdetails()
        name="bahadur"
        empcode = 223
        print(f"Employee code for {name} is {empcode} ")


p= Person()
e= Employee()
pr = Programmer()
# print(pr.company)
''' We are calling company variable using object of child class programmer. 
Company vairble is defined in  Person and Employee class but 
company is called Employee class because the employee class is parent class for programmer class
if company is not defined in Employee then company will be called from Person class
Person is parent class to EMployee and employee is parent to programmer'''
p.getempdetails()
e.getempdetails()
pr.getempdetails()