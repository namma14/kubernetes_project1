file = open('test.txt','r')
#read 1st line
print(file.readline(),end="") # readline function helps to read 1 line at a time. We need to provide more readline functions if we want to read more lines from txt file
#read 2nd line
print(file.readline(),end="")
# read 3rd line 
print(file.readline(),end="")
# if we want to read more lines then use readline method