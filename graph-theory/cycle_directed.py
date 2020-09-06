class Graph:
    def __init__(self,edges,N):

        #a list of lists to represent adjacency list
        self.adj_list = [[] for _ in range(N)]

        #add edges to the directed graph
        for src,dst in edges:
            self.adj_list[src].append(dst)

#perform DFS on graph and set departure time of all vertices
def DFS(graph,v,discovered,departure,time):
    
    #mark current node as discovered
    discovered[v] = True

    #do for every edge
    for u in graph.adj_list[v]:
        if not discovered[u]:
            time = DFS(graph,u,discovered,departure,time)

    #ready to backtrack
    #set of departure time of vertex v
    departure[v] = time
    time += 1

    return time

def is_DAG(graph,N):

    #stores vertex is discovered or not
    discovered = [False] * N

    #stores departure time of a vertex in DFS
    departure = [None] * N

    #initialize time's value
    time = 0

    #do dfs from all undiscovered vertices to visit all connected components of graph
    for i in range(N):
        if not discovered[i]:
            time = DFS(graph,i,discovered,departure,time)

    #check if given directed graph is DAG or not
    for u in range(N):

        for v in graph.adj_list[u]:

            if departure[u] <= departure[v]:
                return False

    return False




#DFS-2 geekforgeeks 
from collections import defaultdict

class Graph2:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def dfs_visit(self,v,visited,recstack):
        
        #mark current node as visited and adds to recursion stack
        visited[v] = True
        recstack[v] = True

        #recur for all neighbors, if any neighbor is visited and in recstack, graph is cyclic
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.dfs_visit(neighbor,visited,recstack):
                    return True
            elif recstack[neighbor]:
                return True

        #the node needs to be popped from recursion stack before function ends
        recstack[v] = False
        return False

    def is_cyclic(self):
        visited = [False]*self.V
        recstack = [False]*self.V

        for node in range(self.V):
            if not visited[node]:
                if self.dfs_visit(node,visited,recstack):
                    return True

        return False

g = Graph2(4)
g.add_edge(0,1)
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
if g.isCyclic() == 1: 
    print "Graph has a cycle"
else: 
    print "Graph has no cycle"