# def rotateArray(arr, n, d):
#     temp = []
#     i = 0
#     while (i < d): # loop will create a list which need to be placed at end from front
#         temp.append(arr[i])
#         i = i + 1
    
#     i = 0
#     while (d < n): 
#         arr[i] = arr[d] # loop will create a list which would move the remaining list from front to end
#         i = i + 1
#         d = d + 1
#     arr[:] = arr[: i] + temp
#     return arr
 
 
# # Driver function to test above function
# arr = [1, 2, 3, 4, 5, 6, 7]
# print("Array after left rotation is: ", end=' ')
# print(rotateArray(arr, len(arr), 3))

# Method2: Python Program for Array Rotation Using Rotate one by one
def leftRotate(arr, d, n):
    for i in range(d): # running loop for d times i.e numbers by which list we want to rotate
        temp=arr[0] # storing 1st element to temp
        for i in range(n-1): # running loop for array
            arr[i]=arr[i+1] # moving the values defined in array by 1 place upward
        arr[n-1]=temp # passing the value of 1st element of array stored in temp to last position of array
    print(arr)
 
 
# # utility function to print an array */
# def printArray(arr,size):
#     for i in range(size):
#         print ("%d"% arr[i],end=" ")
 
  
# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
d=2
n=len(arr)
leftRotate(arr, d, n)
# printArray(arr, 7)