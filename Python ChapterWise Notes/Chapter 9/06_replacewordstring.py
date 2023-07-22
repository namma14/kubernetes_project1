with open('test2.txt','r') as f:
    str1=f.read()
# 1st method without if condition
str1 = str1.replace ('Donkey',"########")
    # print(str1)
with open ('test2.txt','w') as f:
    f.write(str1)
# 2nd method via if condition
if "Donkey" in str1:
    str1 = str1.replace ('Donkey',"########")
    with open ('test2.txt','w') as f:
        f.write(str1)
else:
    print("Donkey not available")