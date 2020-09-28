def partition(array,start,end):
    pivot = array[start]
    low = start+1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and array[high] >= pivot:
            high -= 1

        #opposite process of the one above
        while low <= high and array[low] <= pivot:
            low += 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            array[low], array[high] = array[high], array[low]
            #the loop continues
        else:
            #we exit out the loop
            break

    array[start],array[high] = array[high], array[start]
    return high

def Quick_sort(array,start,end):
    if start >= end:
        return
    p = partition(array,start,end)
    Quick_sort(array,start,p-1)
    Quick_sort(array,p+1,end)

