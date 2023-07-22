# writing a password to generate a random password
# Method1: Using Random Module
import random
import string

letter = string.ascii_lowercase
Letter1 = string.ascii_uppercase
spcl = string.digits
num = string.punctuation
password = letter+Letter1+spcl+num
# print(password)
pwd =''
for i in range(12) :
    pwd += random.choice(password)
print("Password generated using random.choice is: ",pwd)

#Method 2: Using secrets module
import secrets
import string

letter = string.ascii_letters
spcl = string.digits
num = string.punctuation

alphabet = letter+spcl+num
pwd1 =''
for i in range(12):
    pwd1 += secrets.choice(alphabet)
print("Password generated using secrets module",pwd1)

# 3rd Method: using random.shuffle
import random
import string

if __name__ == "__main__":

    str1 =[]
    str1.extend(list(string.ascii_letters))
    str1.extend(list(string.digits))
    str1.extend(list(string.punctuation))
    str1.extend(list(string.whitespace))

    random.shuffle(str1)

    pwdlen = int(input("Enter length of password: "))

    password = ("".join(str1[0:pwdlen]))
    print("Password generated using random.shuffle is : ",password)

# 4th Method: using random.sample
import random
import string

if __name__ == "__main__":

    str1 = []
    str1.extend(list(string.ascii_letters))
    str1.extend(list(string.digits))
    str1.extend(list(string.punctuation))
    str1.extend(list(string.whitespace))

    pwdlen = int(input("Enter length of password: "))
    password1 = random.sample(str1,pwdlen)
    print("Password generated using random.sample is","".join(password1))
    # password = ("".join(str1[0:pwdlen]))
    # print("Password is: ",password)