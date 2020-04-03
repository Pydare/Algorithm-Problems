def ordering_an_array(arr):
    i = 0
    while i <= len(arr)-1:
        #comparing and swapping with the next 3 indices
        a = i+1
        b = i+2
        c = i+3
        d = i+4
        if a <= len(arr)-1:
            if arr[i] > arr[a]:
                arr[i],arr[a] = arr[a],arr[i]
        if b <= len(arr)-1:
            if arr[i] > arr[b] and b <= len(arr):
                arr[i],arr[b] = arr[b],arr[i]
        if c <= len(arr)-1:
            if arr[i] > arr[c] and b <= len(arr):
                arr[i],arr[c] = arr[c],arr[i]
        if d <= len(arr)-1:
            if arr[i] > arr[d] and d <= len(arr):
                arr[i],arr[d] = arr[d],arr[i]
        i += 1
    return arr


print(ordering_an_array([10, 9, 8, 7, 4, 70, 60, 50]))
            
            