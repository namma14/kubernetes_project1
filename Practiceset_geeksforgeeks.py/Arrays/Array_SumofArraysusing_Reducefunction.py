# Writing a prog to find sum of arrays using Reduce functionality
from functools import reduce

def red_arr_sum(self):
    # Defining Lamda function
    lamdasum = lambda a,b:a+b
    # Reduce function to give sum of array using Lamda
    val = reduce(lamdasum,arr)
    return (val)

if __name__=="__main__":
    # defining array
    arr = [1,2,3,4,5]
    # Calling function
    ras = red_arr_sum(arr)
    # printing value of Sum
    print(ras)