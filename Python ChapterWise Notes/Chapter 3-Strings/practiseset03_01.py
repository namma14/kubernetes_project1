# find double spaces in a string
strs = 'Hey!  master  how are you'
a= strs.find('  ')
print(a)
# a=5
# b=6
# print(a>b)
# strs = strs.replace ("  "," ")
# print(strs)
# ifelse worked. 
if a!= -1:
   strs=strs.replace("  "," ")
   print(strs)
   a= strs.find('  ')
   print(a)
else:
   print('No More Double Spaces')
