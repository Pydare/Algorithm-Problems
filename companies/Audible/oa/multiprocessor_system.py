import heapq, math

def schedule_process(num, ability, processes):
    count = 0
    ability = [-1*i for i in ability]
    heapq.heapify(ability)

    while num:
        print(ability, processes)
        node = -heapq.heappop(ability)
        if node > processes:
            continue
        else:
            processes -= node
            count += 1
            node = math.floor(node / 2)
            heapq.heappush(ability, -node)

        if processes == 0:
            break

    return count

ans = schedule_process(5, [3, 1,7,2,4], 15)
print(ans)