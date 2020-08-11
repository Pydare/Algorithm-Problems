d = {5:4,2:3,1:1,6:2}
l = [4,56,7,1,10]
m = [(5,4), (2,3), (1,1), (6,2)]
import heapq
k = 2
res = heapq.nlargest(k, d.keys(), key=d.get)
res2 = heapq.nlargest(k,l)
#print(res)

ids = {1:[]}
visited = {user:False for user in ids[1]}
l.remove(10)
print(l)
