import heapq

random = [57,32,2,90,2,1,12,44,41,76,18,9,32]
q = []

for num in random:
    heapq.heappush(q,num)

while q:
    temp = heapq.heappop(q)
    print(temp)