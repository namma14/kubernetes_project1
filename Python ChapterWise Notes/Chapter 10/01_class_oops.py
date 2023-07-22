# creating a prog to understand oops concepts
class Empoyee: # defined class in pascal nototations
    company = "Google" # class Attributes
    salary = 500 #class Attributes.

rajesh = Empoyee () # Insatancetiation
Karan = Empoyee () # Insatancetiation

# Salary is defined as class attribute, we can also define same as Instance/object attributes
rajesh.salary = 100 # Instance Attribute. Pyhton uses Instance attributes if defined else uses class atributes

# Company is defined as class attribute, we can also define same as Instance/object attributes
Karan.company = "YouTube" # Instance Attribute. Pyhton uses Instance attributes if defined else uses class atributes

print(rajesh.company) 
print(Karan.company)
print(rajesh.salary)
print(Karan.salary)