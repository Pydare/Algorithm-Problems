import heapq

def team_form(n, score, team, m): 
    team_num, start, end = 0, 0, n-1
    f_heap, l_heap = [0], [0]

    for _ in range(m):
        if start == end:
            heapq.heappush(f_heap, -score[start])
            start += 1
            break
        heapq.heappush(f_heap, -score[start])
        start += 1
        heapq.heappush(l_heap, -score[end])
        end -= 1
        if start > end:
            break

    while team != 0:  # [17, 12, 10, 2, 7, 2, 11, 20, 8 ]
        pop_side = 0
        if l_heap[0] < f_heap[0]:
            team_num += heapq.heappop(l_heap)
            pop_side = 1
        else:
            team_num += heapq.heappop(f_heap)
        if start <= end:
            if pop_side == 0:
                heapq.heappush(f_heap, -score[start])
                start += 1
            else:
                heapq.heappush(l_heap, -score[end])
                end -= 1
        team -= 1

    return -team_num