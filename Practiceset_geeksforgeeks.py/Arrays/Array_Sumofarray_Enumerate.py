# wiriting a function to find sum of array via Enumerate Function
def enumerate_sum(arr):
    sum = 0
    for count,value in  enumerate(arr):
        sum += value
    return sum

# Main funciton
if __name__ =="__main__":
    arr = [1,2,3,4,5]
    es = enumerate_sum(arr)
    print(es)