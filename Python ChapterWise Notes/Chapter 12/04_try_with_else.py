# #writing a prog to use else with try

def incnumber(number):
        try:
         z= int(number)+1
         print(z)
        except:
            raise ValueError("Enter Integer value")
        else:
            print("Successful") # the else portion will run only when exception doesn't occur

a = incnumber(5)
# print(a)
# number = int(input("Enter Number"))

# try:
#     z=int(number)+1

# except:
#         raise ValueError("Enter Integer value")
# else:
#         print("SUccessful")