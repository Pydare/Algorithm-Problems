def bubbleSort(L):
    for passnum in range(len(L)-1,0,-1):
        for i in range(passnum):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
    print(L)

L = [34,22,4,56,71,99,34,21,15]
bubbleSort(L)
