def binarySearch(arr, target):
    left , right = 0 , len(arr) -1
    
    while(left<right):
        mid = left + (right-left)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            left = mid+1
        else:
            right = mid - 1
    return -1

array = [1,2,3,4,5,6,7,8,9,10]
target = 8
result = binarySearch(array , target)
if result != -1:
    print("Target found at " , result)
else:
    print("Target not found")
