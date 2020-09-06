from collections import defaultdict
"""
disjoint sets are used to find cycle in a non-directed graph
"""
class Graph:
    def __init__(self,vertices):
        self.V = vertices #no. of vertices
        self.graph = defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)
    
    def find_parent(self,parent,i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent,parent[i])

    def union(self,parent,x,y):
        x_set = self.find_parent(parent,x)
        y_set = self.find_parent(parent,y)
        parent[x_set] = y_set

    def is_cyclic(self):

        #allocate memory for creating V subsets and initialize all subsets as single element sets
        parent = [-1]*(self.V)

        #iterate through all edges of graph, find subset of both vertices
        #of every edge, if both are same, there is cycle in graph
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent,i)
                y = self.find_parent(parent,j)
                if x==y:
                    return True
                self.union(parent,x,y)
        return False 