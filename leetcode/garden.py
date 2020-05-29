from collections import defaultdict

def gardenNoAdj(N, paths):
    graph = defaultdict(list)
    for frm,to in paths:
        graph[frm].append(to)
        graph[to].append(frm)
    output = [0]*(N+1)
    for frm in range(1,N+1):
        taken = []
        for to in graph[frm]:
            taken.append(output[to])
        flower = 1 
        for i in range(4):
            if flower in taken:
                flower+=1 
            else:
                break
        output[frm] = flower 
    return output[1:]