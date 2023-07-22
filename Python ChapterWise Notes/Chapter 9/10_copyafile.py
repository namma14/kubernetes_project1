# wite a prog to make a copy of file

with open('this.txt') as f:
    str1=f.read()

with open('copy.txt','w') as f:
    f.write(str1)


