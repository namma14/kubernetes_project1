with open ('log.txt','r') as f:
    str1 = f.read().lower() # lower() function is used to convert all the content in log.txt file in lower case

if "Python" in str1.lower(): # lower() function ko yha pe bhi use kar sakte h
    print("Python available")
    print (f)
else:
    print("Pyhton kha h?")
