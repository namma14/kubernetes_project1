# __str__ and __len__ dunder method.
class Employee():
    def newstr(self,str1):
        self.str1 = str1
    def __len__(self,txt):
        print ("lenght of string is: ", len(self.str1))

e = Employee()
e.str1 = "Hello"
e.newstr("hello")
# e.__len__()
len('Hello')()

# class YString(str):
#     def __init__(self, text):
#         super().__init__()

#     def __str__(self):
#         """Display string as lowercase except for Ys that are uppercase"""
#         return self.lower().replace("y", "Y")

#     def __len__(self):
#         """Returns the number of Ys in the string"""
#         return self.lower().count("y")
# message = YString("Real Python? Yes! Start reading today to learn Python")
# print(message)