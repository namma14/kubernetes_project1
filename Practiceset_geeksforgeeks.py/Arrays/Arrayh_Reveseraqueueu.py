class Sol():
    def revstr(self,arr):
        for i in range(len(arr),0,-1):
            print(arr[i-1])

if __name__=="__main__":
    s=Sol()
    arr=[4,3,1,10,2,6]
    s.revstr(arr)
    

# Method 2: without Class and Function
# arr=[4,3,1,10,2,6]
# print(len(arr))

# for i in range(len(arr),1,-1):
#     print(arr[i-2])