# writing a prog to a new list out of existing list
# Without List Comparison
list_old=[112,14,15,34,465,233,5.6,78,34,90]
list_new=[]
for i in list_old:
    if i>100:
        list_new.append(i)
print(list_new)
#List Comparison: It is a method to create a list from existing list. This method can be used to create dictionary and set as well
list1=[1,2,3,34,54,232,56,89,78,56,34,10]
list2 = [item for item in list1 if item%2==0] # new method to create a list from existing list
print(list2)

# creating set using list comparison
l1=[1,2,3,4,5,6,34,46,2335,3455,1,2,3,4,5,6]
l2={i for i in l1}
print(l2) # repeated values are removed, when a set is created
print(type(l2))

# Dictionary
list_old=[112,14,15,34,465,233,5.6,78,34,90]
list1=   [1,2,3,34,54,232,56,89,78,56,34,10]
dict1 = dict(zip(list_old,list1))
print(dict1)
# Dictionary using comparison
data = [('kumar',5), ('suraj',9)]
dict1 = [(keys,values) for  keys,values in data ]
print(dict(dict1))


