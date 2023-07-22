# 1st method via ifelse method
l1=["arun","sachin","saurabh","theevandi"]
name = input("Enter name \n")
# print(l1[0][0])
# x=l1.index(name)
# print(x)
# if (l1[x][0] =="s"):
#          print ("Hello", l1[x])
# else:
#          print("Bye!!")
# 2nd method via for loop
l2 = ["karan","shanti","sunil","anil"]
for i in l2:
        if i.startswith("s"):
                print("Hello", i)
