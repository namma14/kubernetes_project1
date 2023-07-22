list1 = ["donkey", "kaddu", "don","mote"]

with open ('test2.txt','r') as f:
    str1=f.read()

for i in list1:
    str1 = str1.replace (i, "*****")
    with open ('test2.txt','w') as f:
        f.write(str1)

