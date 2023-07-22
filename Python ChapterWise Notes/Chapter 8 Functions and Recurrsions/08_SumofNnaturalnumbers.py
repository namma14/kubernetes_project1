# calculate sum of N natural number
# Find sum of first 5 natural numbers = 1+2+3+4+5 or 5 + sum(4) i.e n +sum(n-1)
#logic sum (Natural Numbers) = N + Sum(N-1)
def sumnatural(n):
    if n ==1:
          return n
    else:
          return n + sumnatural(n-1)

n = int(input("Enter number to calculate Sum: "))
if n<=0:
    print("Please enter number greater than 0")
else:
         print(f"sum of {n} natural numbers is {sumnatural(n)}")
