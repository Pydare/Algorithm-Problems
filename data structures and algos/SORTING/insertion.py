def insertionSort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = temp 
    print(a)

insertionSort([67,45,33,6,34,10,420,8,31,13,29])