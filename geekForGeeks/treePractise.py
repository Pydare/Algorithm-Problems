class Node:
    def __init__(self,val):
        self.val = val
        self.count = 1
        self.left = None
        self.right = None


#print path from root to a given node in binary tree
def path(root,key,l):
    if root is None:
        return
    l.append(root.val)
    
    path(root.left,key,l)
    path(root.right,key,l)
    
    if root.val == key:
        return l
    l.pop()

# Driver Code 
if __name__ == '__main__': 
      
    # binary tree formation  
    root = Node(1)  
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5)  
    root.right.left = Node(6)  
    root.right.right = Node(7)  
          
    x = 5
    ans = path(root, x, [])
    print(ans)
