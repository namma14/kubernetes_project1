# Writing a prog to open three files if any of the file is not available then use exception handling

def openfiles():
    try:
        with open ('test5.txt','r') as tr:
            str1=tr.read()
            print("***** Content of File1 ******")
            print(str1)
    except FileNotFoundError:
        print("***** Error Message ******")
        print("File is not available")
    
    try:
        with open('this5.txt','r') as thr:
            str2=thr.read()
            print("***** Content of File2 ******")
            print(str2)
    except FileNotFoundError:
        print("***** Error Message ******")
        print("File is not available")
    try:
        with open('this5.txt','r') as thr2:
            str3=thr2.read()
            print("***** Content of File3 ******")
            print(str3)
    except FileNotFoundError:
        print("***** Error Message ******")
        print("File is not available")
    finally:
        print("All files are read")
    
read = openfiles()
# 2nd Method
def readfiles(filename):
    try:
        with open(filename,'r') as f:
            print(f"***** Content of file {filename} ******")
            print(f.read())
    except FileNotFoundError:
        print("***** Error Message ******")
        print(f"File {filename} is not available")

wr = readfiles('this.txt')
wr = readfiles('test.txt')
wr = readfiles('test5.txt')