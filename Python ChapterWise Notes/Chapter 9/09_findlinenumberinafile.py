# to find a word in a file and linenumber at which the word is available in file
str1 = True
i=1
with open('log.txt','r') as f:
      while str1:
        str1=f.readline().lower()
        if "python" in str1:
            print (str1)
            print (f"Yes! Pyhton is available at line number {i}")
        i+=1
