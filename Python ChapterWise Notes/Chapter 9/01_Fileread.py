# Use open function to read the contents of file
# file = open('test.txt','r') # by default the text file is accessed in read file. We don't have to specify read option
file = open("test.txt")
print(file.read()) # to read complete file
print(file.read(5)) # we can specify how many characters we want to read from a file
file.close()