def shellSort(a):
    h = int(input('Enter the maximum number of pass: '))
    while h>=1:
        for i in range(h,len(a)):
            temp = a[i]
            j = i-h
            while j>=0 and a[j]>temp:
                a[j+h] = a[j]
                j = j-h
            a[j+h] = temp
        h = h-2
    print(a)


shellSort([67,45,33,6,34,10,420,8,31,13,29])