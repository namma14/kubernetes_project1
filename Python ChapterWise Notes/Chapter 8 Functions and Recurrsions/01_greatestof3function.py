def greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        else: 
            return c
    else:
        if b>c:
                return b
        else: 
            return c


print(greatest(254,96,7))
