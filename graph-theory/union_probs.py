class Solution:
    def find_parent(self,parent,i):
        if parent[i] == -1:
            return i
        else:
            parent[i] = self.find_parent(parent,parent[i])
            return parent[i]
            
    def union(self,parent,x,y,size):
        px = self.find_parent(parent,x)
        py = self.find_parent(parent,y)
        
        if px == py:
            return
        elif size[px] < size[py]:
            parent[px] = py
            size[py] += px
        else:
            parent[py] = px
            size[px] += py
    
    
    def findCircleNum(self, M):
        parent = [-1]*len(M)
        size = [1]*len(M)
        
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1 and i != j:
                    self.union(parent,i,j,size)
                    
        count = 0
        for i in parent:
            if i == -1:
                count += 1
        return count
        
        
        
                