#DFS
def cycle_exists(g):
    marked = {u:False for u in g}
    found_cycle = [False]

    for u in g:
        if not marked[u]:
            dfs_visit(g,u,found_cycle,u,marked)
        if found_cycle[0]:
            break
    return found_cycle[0]

def dfs_visit(g,u,found_cycle,pred_node,marked):
    if found_cycle[0]:
        return
    marked[u] = True
    for v in g[u]:
        if marked[v] and v != pred_node:
            found_cycle[0] = True
            return
        if not marked[v]:
            dfs_visit(g,v,found_cycle,u,marked)


#BFS
from collections import deque

class Graph:
    def __init__(self,edges,N):
        #a  list of lists to represent an adjacency list
        self.adj_list = [[] for _ in range(N)]

        #add edges to the undirected graph
        for src,dst in edges:
            self.adj_list[src].append(dst)
            self.adj_list[dst].append(src)

def BFS(graph,src,N):

    #stores vertex that has been seen or not
    discovered = [False]*N

    #mark source vertex as discorvered
    discovered[src] = True

    #create a queue used to do BFS
    q = deque()

    #push source vertex and its parent info into queue
    q.append((src,-1))

    #loop till queue is empty
    while q:

        #pop front node from queue and print it
        v,parent = q.popleft()

        #do for every edge (v -> u)
        for u in graph.adj_list[v]:
            if not discovered[u]:
                #mark it as discovered
                discovered[u] = True

                #construct the queue node containing info about vertex and push to queue
                q.append((u,v))
            
            #u is discovered and u is not a parent
            elif u != parent:
                #cross-edge found
                return True

    #else no cycle is found
    return False