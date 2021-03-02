
def median(first, last, mid):
    if ( first - last) * (mid - first) >= 0:
        return first
    elif (last - first) * (mid - last) >= 0:
        return last
    else:
        return mid

def partition_modified_median(array, low, high):
    small = array[low]
    high = array[high - 1]
    length = high - low
    middle = array[low + length // 2]
    pivot = median(small, high, middle)
    pivotindex = array.index(pivot)
    array[pivotindex] = array[low]
    array[low] = pivot
    i = low + 1
    for j in range(low + 1, high):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    highEndVal = array[low]
    array[low] = array[i - 1]
    array[i - 1] = highEndVal
    return i - 1

def quicksort_median(array, low_Index, high_Index):
    
    if low_Index+ 10  <= high_Index:
        new_pivot_Index = partition_modified_median(array, low_Index, high_Index)
        quicksort_median(array, low_Index, new_pivot_Index)
        quicksort_median(array, new_pivot_Index + 1, high_Index)

    else:
        insertion_sortt(array,low_Index,high_Index)

def insertion_sortt(array,first,last):
    for i in range(first, last):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            j = j - 1

def mquick_sort(array):
    quicksort_median(array, 0, len(array))
    return array

array=[2,1,6,9,10,11,60,14,15,22,8,88,40,24,36,75,888,14]
sorted_array=mquick_sort(array)
print(sorted_array)