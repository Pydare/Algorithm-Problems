arr = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]

n = len(arr)

for i in range(n):
    for j in range(i,n):
        arr[j][i], arr[i][j] = arr[i][j], arr[j][i]

for i in range(n):
    arr[i].reverse()
print(arr)
        



