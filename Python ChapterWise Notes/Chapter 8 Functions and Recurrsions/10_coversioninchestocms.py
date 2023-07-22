# write a prog to convert inches to cms
# logic 1 inc = 2.54 cms
def conv(length):
    return length * 2.54

inches = int(input("Enter the Lenght in Inches: "))
cms = conv(inches)
print(f"The lenghth in cms is {cms}")