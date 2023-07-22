with open('this.txt') as f:
    str1=f.read()
with open('copy.txt') as f:
    str2=f.read()

if str1==str2:
    print("Files are Identical")
else:
    print("Files are Not Identical")
