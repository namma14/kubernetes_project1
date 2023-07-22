n=6
for i in range (1,n+1):
    print(" " * (n-i) + " *" * (i)) # to print trainagle star pattern
for i in range (n-1,-1,-1):
    print(" " * (n-i) + " *" * (i+1)) # to print inverted triangle star pattern