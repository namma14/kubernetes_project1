'''Writing a prog to enumerate a list
Enumerate function adds counter to an list and returns it'''
# List/indexing of all elements of a list/set without enumerate
list1=[1,2,'hello', False,3.7,8]
index = 0
for items in list1:
    print(index,items)
    index += 1
print("*******************************")

#Enumerate: Listing of all elements in a list/set
for index1,items1 in enumerate(list1):
    print(index1,items1)