# Explaining single inheritance and concepts
class employee:
    company = "Google"
    def getDetails(self):
        print("I am an Employee")
    
class programmer(employee): # programmer is a child class derived from parent employee class
        company = "Youtube"
        def getprogrammerdetails(self):
            print(f"I am a programmer from company {self.company}")
            
        def getDetails(self):
            print("I am an Employee from programmer class") 
            '''# defined the same function in child class.
            When child class getDetails function is called, 
            it will be called form child class not from parent class 
            We have overrided the parent class function in child class'''

e=employee()
p=programmer()
e.getDetails()
p.getprogrammerdetails()
p.getDetails()