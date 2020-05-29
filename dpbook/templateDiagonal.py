n = 6
arr = [[0 for i in range(n)] for _ in range(n)]

temp = [9,4,3,1,7,2]

#handling the main diagonal of the 2d array
for i in range(n):
    arr[i][i] = temp[i]

#handling upper diagonal of the 2d array
for i in range(0,n-1):
    for j in range(1,n-i):
        k = j+i 
        arr[i][k] = arr[i][k-1] + temp[k]

print(arr)