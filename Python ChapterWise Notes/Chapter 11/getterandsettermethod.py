'''Writing a prog to understand getter and setter
Getter: A method that allows you to access an attribute in a given class
Setter: A method that allows you to set or mutate the value of an attribute in a class'''
class Employee:
    company = "India"
    salary = 100
    salarybonus = 50


    @property # getter is defined, now we can call totalsalary function as variable.
    def totalsalary(Self):
        print("Salary: ",Self.salary)
        print("SalaryBonus: ",Self.salarybonus)
        return Self.salary+Self.salarybonus
    
    @totalsalary.setter 
    def totalsalary (self,val):
        self.salarybonus=val-self.salary
        print("val",val)
        print("salary1", self.salary)
        print("salarybonu1", self.salarybonus)

e = Employee()
# print("Total Salary is: ",e.totalsalary())
print("Total Salary is: ",e.totalsalary) # while calling function totalsalary i have to call it as a function
e.totalsalary = 200
