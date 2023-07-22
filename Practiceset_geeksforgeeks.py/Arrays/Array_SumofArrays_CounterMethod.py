# Wiriting a prog to find sum of arrays using Counter Method
# Counter class is used to count the occurrences of elements in the input array
from collections import Counter
def counter_array_sum(arr):
    ar1 = Counter(arr)
    sum=0
    for a,b in ar1.items():
        sum += a*b
    return sum

# Main Functino
if __name__ == '__main__':
    arr=[1,2,2,3,3,3,4,5]
    cas=counter_array_sum(arr)
    print(cas)
# ar1 = Counter(arr)
# print("Items",ar1.items())
# # print(ar1)
# sum=0
# for a,b in ar1.items():
#     sum += a # to find sum of only single value
#     sum += a*b # to find sum of all duplicate value. This would multiply the value with its occurance
# print(sum)