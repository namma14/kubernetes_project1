def avgnumber(*number): # *number is used when variable are not confirmed, we can calc avegare of n number of variables
    sum=0
    for i in number:
        sum = sum+i
    return sum/len(number)

average = avgnumber (2,3,7,3,4,5,63434,664,909)
print ("The average of Numbers is ", average)

# logic
# number = (12,12)
# sum=0
# for i in number:
#         sum = sum+i
# print ("Average of numbers is: ", sum/len(number))