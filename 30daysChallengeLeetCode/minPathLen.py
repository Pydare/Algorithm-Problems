l = [[0]*3]*3
m = [[1,3,1],[1,5,1,],[4,2,1]]

temp = 0
for i in range(1,len(m)):
    m[i][0] += m[i-1][0]

for i in range(1,len(m[0])):
    m[0][i] += m[0][i-1]

print(m)