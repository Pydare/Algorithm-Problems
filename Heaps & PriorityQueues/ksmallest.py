import heapq

"""
min-heap: k largest
max-heap: k smallest

[57,90]
"""

random = [57,32,2,90,2,1,12,44,41,76,18,9,32]
random = [-1*i  for i in random]

def k_smallest(random,k):
    res = random[:k]
    heapq.heapify(res) 

    for num in (random[k:]): #[57,90]
        if num > res[0]:
            heapq.heappop(res)
            heapq.heappush(res,num)
    return [-1*i for i in res]

res = k_smallest(random,2)
print(res)
