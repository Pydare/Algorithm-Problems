"""
used in cyclic detection of undirected graphs
"""
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        

    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def find_parent(self,parent,i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent,parent[i])

    def find_parent_path_compression(self,parent,i):
        if parent[i] == -1:
            return i
        else:
            parent[i] = self.find_parent_path_compression(parent,parent[i])
            return parent[i]
        # else: #iterative
        #     j = i
        #     while parent[j] != -1:
        #         parent[j] = parent[parent[j]]
        #         j = parent[j]
        #     return j


    def weighted_union(self,parent,size,x,y):
        x_set = self.find_parent(parent,x)
        y_set = self.find_parent(parent,y)
        if size[x_set] < size[y_set]:
            parent[x_set] = y_set
            size[y_set] += x_set
        elif size[x_set] > size[y_set]:
            parent[y_set] = x_set
            size[x_set] += y_set
        else:
            return 

    def is_cyclic(self):
        parent = [-1]*self.V

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent,i)
                y = self.find_parent(parent,j)
                if x == y:
                    return True
                self.union(parent,x,y)
        return False 