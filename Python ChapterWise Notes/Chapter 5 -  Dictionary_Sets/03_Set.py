a={1,2,3,5}
print(a)
b = set()
print(type(b))
b.add(5,) # to add a value to set use add() function
b.add(6)
b.add((4,6,7,8)) # we can add tuple to set as the value of tuple are not changeable as set doesn't allow mutation or changing
print(b)
# b.add([2,3,4]) # we can't add list to set as the value of list are changeable and set doesn't allow mutation or changing
# b.add({1:2,3:4}) # we can't add dictionary to set as the value of dictionary are changeable and set doesn't allow mutation or changing
print(len(b)) # to get the len/no of items available in set
b.remove(6) # to remove any value from set
b.pop() # removes any random value from set
# b.clear()
b.union({2,3})
print(b)