# write a prog to find largets number in array
# Method1: using reduce and max function
from functools import reduce
class largest:
    def largestnum(self,arr):
        val = reduce(max,arr)
        return val
# Main Function
if __name__=="__main__":
    arr=[4,3,15,10,2,6]
    lar=largest()
    print(lar.largestnum(arr))

# 2n Method: using general code
class largestnew:
    def largestnum1(self,arr):
        max=0
        for i in range(len(arr)):
            if arr[i]>max:
                max=arr[i]
        return max

# Main Function
if __name__=="__main__":
    arr=[4,3,15,10,2,6]
    lar=largestnew()
    print(lar.largestnum1(arr))

# 3rd Method: Using Sort Method
class largenew:
    def largenum(self,arr):
        arr.sort() # largest number will be at the end
        return arr[len(arr)-1] # to print largest number which is at end
      # arr.sort(reverse=True) # largest number will be at the front at 0 position
      # return arr[0] # to print largest number which is in front at 0
# Main Function
if __name__=="__main__":
    arr=[4,3,15,10,2,6]
    lar=largenew()
    print(lar.largenum(arr))   

# Method 4: Using Lamda Function
arr=[4,3,15,10,20,6]
# print(max(arr))
val = lambda x:x
largest = max(arr,key=val) # if we have to pass lamda in max function use (key=lamda variabel:expressions)
print(largest)
