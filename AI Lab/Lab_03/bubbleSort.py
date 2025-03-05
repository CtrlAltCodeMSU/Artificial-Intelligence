def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        swapped = False ;
        for j in range (n - i - 1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]
                swapped = True
        if not swapped:
            break
        
array = [1,80,4,0,70,6,40,10]
bubbleSort(array)
print("Sorted Array is: " , array)
    