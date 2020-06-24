intervals = [[1,3],[2,6],[8,10],[15,18]]
l = []
for i in range(len(intervals)):
    for j in range(len(intervals[i])):
        l.append(intervals[i][j])
k = 1      
for i in range(1,len(l)):
    if l[i] > l[i-1]:
        l[k] = l[i]
        k += 1
l = l[:k+1]
print(l)