from functools import reduce
# Method 1: to calculate maximum from a list without in-bult function max()


def maximum(n):
    global k
    k = 0
    for i in n:
        if i > k:
            k = i
    print(k)


n1 = [29, 35, 34, 23, 15]
maximum(n1)


list1 = [23,34,53,25]
print(reduce(max,list1))


