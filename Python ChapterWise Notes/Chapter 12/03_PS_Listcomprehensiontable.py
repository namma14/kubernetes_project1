#wriet a prog to print multiplication of user entered number
num = int(input("Enter Number: "))
list1 = [num*i for i in range(1,11)]
print(list1)
with open('this5.txt','a') as f:
    f.write(str(list1))
    f.write('\n')

# for i in range (1,11):
#     list1.append(num*i)

# print(list1)
