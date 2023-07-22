# write a prog to rename a file
import os

with open('hiscore.txt') as f:
    str1=f.read()

with open ('renamed_by_python.txt','w') as f:
    f.write(str1)

os.remove("hiscore.txt")
