# write a prog to check if a student is pass or fail. total passing marks is 40% and 33% min required in each of 3 subjects
import math
s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))

total_marks = s1+s2+s3 
print(total_marks/3)
if (total_marks/3<40 or s1<33 or s2<33 or s3<33):
    print("Fail")
else:
    print("pass")
# 2nd method
if (s1<33 or s2<33 or s3<33):
    print("Fail!, marks in 1 of the subject is lessthan 33")
elif (s1+s2+s3)/3<40:
    print("Fail! Total Pecentange is less than 40%")
else:
    print("Passed, Marks in each subject is greater than 33 and total marks are also greater than 40%")
