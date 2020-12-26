#DFS
#assuming g is a defaultdict
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

###################latest cycle detection from graph valid tree ---> BEST GUY FOR THE JOB
from collections import defaultdict
def valid_tree(n,edges):
    if len(edges) != n-1: return False
    adj_list = defaultdict(list)

    for x,y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    parent = {0:-1}
    stack = [0]

    while stack:
        node = stack.pop()
        for nei in adj_list[node]:
            if nei == parent[node]:
                continue
            if nei in parent:
                return False
            parent[nei] = node
            stack.append(nei)
    
    return len(parent) == n # If the graph is fully connected, then every node must have been seen

def valid_tree_recur(n,edges):
    if len(edges) != n-1: 
        return False
    adj_list = defaultdict(list)

    for x,y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)

    seen = set()
    def dfs(node,parent):
        if node in seen: 
            return
        seen.add(node)
        for nei in adj_list[node]:
            if nei == parent:
                continue
            if nei in seen:
                return False
            result = dfs(nei,node)
            if not result: 
                return False 
        return True

    return dfs(0,-1) and len(seen) == n # If the graph is fully connected, then every node must have been seen

#advanced dfs
def valid_tree_adv(n,edges):
    if len(edges) != n-1: return False

    adj_list = defaultdict(list)
    for x,y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)

    seen = set()

    def dfs(node):
        if node in seen:
            return
        seen.add(node)
        for nei in adj_list[node]:
            dfs(nei)
    dfs(0)
    return len(seen) == n # If the graph is fully connected, then every node must have been seen

##################################
#UNION FIND SOLUTION
class UnionFind:
    def __init__(self,n):
        self.parent = [-1 for _ in range(n)]
        self.size = [1]*n

    def find(self,A):
        if self.parent[A] == -1:
            return A
        else:
            self.parent[A] = self.find(self.parent[A])
            return self.parent[A]

    def union(self,A,B):
        root_A = self.find(A)
        root_B = self.find(B)

        if root_A == root_B:
            return False
        if self.size[root_A] < self.size[root_B]:
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
        else:
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
        return True

class Solution3:
    def valid_tree(self,n,edges):
        if len(edges) != n-1: return False

        union_find = UnionFind(n)

        for x,y in edges:
            if not union_find.union(x,y):
                return False

        return True