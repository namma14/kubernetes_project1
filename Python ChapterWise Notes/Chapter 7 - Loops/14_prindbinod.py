# str1 = input("Enter Name: ")
# z= "BINOD"
name = input("Enter Name: ")
# print(z[:2])
# print(len(z))
# print (z[0])
for i in range(len(name)):
     print (name[:i+1])
for j in range (len(name),0,-1):
     print(name[:j-1])
