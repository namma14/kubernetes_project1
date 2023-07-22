class Employee:
    company = "Google"

    def __init__(self,name,salary,location): # this function is selfcalled when class is called. We dont have to make a call separately.
        print("Employee is created")
        self.name = name
        self.salary = salary
        self.location = location
    
    def employeeDetails(self):
        print (f"Name of Employee is {self.name}")
        print (f"Name of Employee is {self.salary}")
        print (f"Name of Employee is {self.location}")

    def GetSalary(self):
        print(f"Salary of Employee from company {self.company} is {self.salary}")

emp1=Employee("nachiketa",12000,"Gurgaon") # Arguments are passed as __init__ function is expecting 3 arguments.
# emp1.salary=100000
emp1.id = 10113
emp1.employeeDetails()
emp1.GetSalary()
