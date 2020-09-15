class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

#DFS
class Soulution:
    def __init__(self):
        #dict to save visited nodes and it's respective clone as key 
        #value pairs respectively
        self.visited = {}

    def clone_graph(self,node):

        if not node:
            return node
        
        #if node was already visited before, return the clone from visited dict
        if node in self.visited:
            return self.visited[node]
        
        #create a clone for given node
        clone_node = Node(node.val,[])

        #the key is original and value is cloned
        self.visited[node] = clone_node

        #iterate through neighbors to generate their clones
        #and prepare a list of cloned neighbors to be added to the cloned node
        if node.neighbors:
            clone_node.neighbors = [self.clone_graph(n) for n in node.neighbors]

        return clone_node


#BFS
from collections import deque
class Soulution2:
    def clone_graph(self,node):
        if not node:
            return node
        
        #dict of node and cloned key val pair
        visited = {}

        q = deque([node])
        visited[node] = Node(node.val,[])

        #start bfs traversal
        while q:
            n = q.popleft()
            #iterate through neighbors of the node
            for neighbor in n.neighbors:
                #clone the neighbor and put in the visited
                visited[neighbor] = Node(neighbor.val,[])
                #add the newly encountered node to the queue
                q.append(neighbor)
            #add the clone of the neighbor to the neighbors of the clone node n
            visited[n].neighbors.append(visited[neighbor])

        #return the clone of the node from visited
        return visited[node]
