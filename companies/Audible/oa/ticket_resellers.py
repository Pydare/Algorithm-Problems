import heapq
def maximum_tickets(arr, k):
    arr = [-i for i in arr]
    heapq.heapify(arr)
    total = 0

    while k > 0:
        node = heapq.heappop(arr)
        total += node
        heapq.heappush(arr, node+1)
        k -= 1

    return -total

ans = maximum_tickets([2,8,4,10,6], 20)
print(ans)