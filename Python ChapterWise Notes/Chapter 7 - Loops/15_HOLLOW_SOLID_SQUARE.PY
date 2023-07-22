# to print solid square
n = 6
for i in range(n):
    for j in range(n):
        # if i == 0 or i == n-1 or j==0 or j==n-1:
            print("*" , end="")
        # else:
            print(" ", end="")
    print()
print ("---------------------------------------------------------")
# 2nd method
for i in range (1,n+1):
      print("* " * n, end="")
      print()
# Print Hollow Square
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j==0 or j==n-1:
            print("*" , end=" ")
        else:
            print(" ", end=" ")
    print() # this print() funtion helps to move to next line while printing
