# Method 1: Generating list of 7 table via for loop
number = 7
list1=[]
for i in range(1,11):
    list1.append(number*i)

list2 = [i*7 for i in range(1,11)] # Method2 generating a multiplication table of 7 via list comparison
print(list1)
print(list2)
newlist = map(str,list1) # map is used to typecast a int list into str list
print(type(newlist))

newlist2 = map(str,list1) # map is used to typecast a int list into str list
print(type(newlist2))

str1 = "\n" .join(newlist)
print(str1)
str2 = "\n" .join(newlist2)
print(str2)

# Method 3 : 
list3 = [str(i*7) for i in range(1,11)] # Method2 generating a multiplication table of 7 via list comparison
# typecasting the list in comparison itself
print("***********************")
print("\n" .join(list3))
