def partition_first(array, leftend, rightend):
    pivot = array[leftend]
    i = leftend + 1
    for j in range(leftend + 1, rightend):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftendval = array[leftend]
    array[leftend] = array[i-1]
    array[i-1] = leftendval
    return i - 1 
def quick_sort1(array, leftindex, rightindex):
   
    if leftindex < rightindex:
        
        newpivotindex = partition_first(array, leftindex, rightindex)
        
        quick_sort1(array, leftindex, newpivotindex) 
        
        quick_sort1(array, newpivotindex + 1, rightindex)
        
arr = [2,1,6,9,10,11,60,14,15,22,8,88,40,24,36,75,888,14] 
n = len(arr) 
quick_sort1(arr, 0, n) 
for i in range(n): 
	print(arr[i])
