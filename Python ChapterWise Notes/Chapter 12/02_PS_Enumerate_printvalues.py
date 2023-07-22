# write a prog to write 3rd,5th and 7th values from list
# it help to add counter/index values to numbers
list = [1, 3, 34, 54, 767, 5, 23, 905, 4, 23, 45, 66, 343, 35]
list1 = []

# for index,i in enumerate (list):
#     if index == 2 or index == 4 or index ==6:
#         print(i)
#         list1.append(i)
# print(list1)

for index, i in enumerate(list):
    # print(i)
    if index == 2 or index == 4 or index == 6:
        index += 1
        list1.append(i)
print(list1)
