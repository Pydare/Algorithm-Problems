n = [21,45,3,27,14,8,10,6,67,50]
for i in range(len(n)-1):
    minIndex = i
    for j in range(i+1,len(n)):
        if n[j] < n[minIndex]:
            j = minIndex
    if i != minIndex:
        n[i], n[minIndex] = n[minIndex], n[i]