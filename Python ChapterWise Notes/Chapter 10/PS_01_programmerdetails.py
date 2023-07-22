# writing a program to store programmers information working at microsoft
class programmer:
    company = "Microsoft"
    def programmerDetails(self):
        print("Programmer Details:- ")
        print(f"Programmer Name is {self.name}")
        print(f"Programmer Name is {self.company}")

Developer=programmer()
Developer.name= "Naveen"
Developer.role = "Lead Developer"
Developer.technology = "Python"
Developer.manager= "Nikunj"
Developer.salary = 100000
Developer.programmerDetails()
Developer1=programmer()
Developer1.name = "Arun"
Developer.role = "Lead Developer"
Developer.technology = "Python"
Developer.manager= "Nikunj"
Developer1.programmerDetails()
# similarly we can print info of other employees as well