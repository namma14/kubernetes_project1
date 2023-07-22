class Employee:
    salary = 100
    increment = 70

    @property
    def salarychange(self):
        print("Current Salary:", self.salary)
        print("Current Increment:", self.increment)
        return self.salary+self.increment

    @salarychange.setter
    def salarychange(self,newsalary):
        self.increment = newsalary - self.salary
        print(newsalary)
        print(self.salary)
        print(self.increment)

e = Employee()
e.salarychange = 200
print(e.salarychange)



