def insertionsort(arr,simulation=False):

    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos>0 and arr[pos-1]>cursor:
            #swap the number down the list
            arr[pos] = arr[pos-1]
            pos = pos-1
        #break  and do the final loop
        arr[pos] = cursor
        
    return arr