def selectionsort:
    for i in range(len(arr)):
        minimum = i

        for j in range(i+1,len(arr)):
            #select the smalles value
            if arr[j] < arr[minimum]:
                minimum = j


        #place it at the front of the sorted end of the array
        arr[minimum],arr[i] = arr[i],arr[minimum]
    return arr
