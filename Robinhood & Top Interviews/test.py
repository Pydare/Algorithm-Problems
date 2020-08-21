l = [1,1,2,2,2,3,3,4,4,4,4,5]

count = {}

for x in l:
    count[x] = count.get(x,0) + 1

print(count)