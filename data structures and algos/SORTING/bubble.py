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


bubbleSort([67,45,33,6,34,10,420,8,31,13,29])