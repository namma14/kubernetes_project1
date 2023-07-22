# Reduce method applier rolling computation on squential pair of elements
from functools import reduce # reduce method is imported from functools module


def additon(a, b):
    return a+b


l1 = [1, 2, 3, 4, 5, 6]
print(reduce(additon, l1)) 
'''reduce method perform rolling computation i.e 1+2 =3 then 3+3 = 6 , 6+4=10 and so on
i.e output of first 2 elements becomes input for next computation'''

#method2 Reduce method with Lamda function

multiply = lambda a,b:a*b

print(reduce(multiply,l1))