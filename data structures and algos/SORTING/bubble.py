def bubbleSort(a):
    for i in range(len(a)-1,0,-1):
        swaps = 0
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
                swaps += 1
        if swaps == 0:
            break
    print(a)


# bubble sort new
def bubble_sort(a):
    n = len(a)

    for i in range(n):
        #flag to allow function terminate if theres nothing to swap
        already_sorted = True
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

                already_sorted = False

        if already_sorted:
            break
        print(a)
    return a

# insertion sort new
def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j] = arr[j+1]
            j -= 1
        arr[j+1] = temp

    return arr


#merge sort new
def merge_sort(arr):

    n = len(arr)
    if n > 1:
        mid = n//2
        left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
        m, n = len(left), len(right)
        i = j = k = 0

        while i<m and j<n:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < m:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n:
            arr[k] = right[j]
            j += 1
            k += 1
    return arr



#quick sort new
def quick_sort(arr):
    sort(arr,0,len(arr)-1)
    return arr

def sort(arr,low,up):
    if low >= up:
        return
    p = partition(arr,low,up)
    sort(arr,low,p-1)
    sort(arr,p+1,up)

def partition(a,low,up):
    pivot = a[low]
    i = low+1
    j = up
    while i <= j:
        while a[i] < pivot and i < up:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i < j:
            a[i],a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            break
    a[low] = a[j]
    a[j] = pivot
    return j

ans = quick_sort([67,45,33,6,34,10,420,8,31,13,29])
print(ans)