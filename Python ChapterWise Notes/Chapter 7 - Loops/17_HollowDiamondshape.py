# print hollow Diamond
n=7
for k in range(n):
        for l in range (n):
             if k+l==3 or l-k==3 or k+l==9 or k-l==3:
                    print("*", end="")
             else:
                    print(" ", end="")
        print()
