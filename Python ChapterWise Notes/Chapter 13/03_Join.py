#wiring a prog for Join function
# join function is used to create a string from iterable objects ex: lits,tuple
l1=['camera','laptop','phone','ipad','harddisk','nvidia graphics card']
k=l1.remove('camera')
l2=[]
print(l1)
sentence = " \n ".join(l1) # "and" is a seprator used. it can be anything. we can use \n for next line as well
#.join(argument) this is the function passed. Argument is the list or tuple object
print(sentence)

for i in l1:
    l2.append(i)
print(l2)


