class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isSibling(root, a , b): 
  
    # Base Case 
    if root is None: 
        return 0
    if ((root.left == a) and (root.right == b)) or ((root.left == b) and (root.right == a)):
        return True
    ans = isSibling(root.left,a,b)
    if ans == True:
        return True
    else:
        return isSibling(root.right,a,b)   

def level(root,x,lev):
    if not root:
        return 0
    if root.val == x:
        return lev
    
    #return level if Node is present in left subtree
    l = level(root.left,x,lev+1)
    if l != 0:
        return l
    #else search in right subtree
    return level(root.right,x,lev+1)

def isCousin(root,a,b):
    if ((level(root,a,1) == level(root, b, 1)) and not (isSibling(root, a, b))):
        return True
    else:
        return False


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.right.right = Node(15) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8)

a = root.left
b = root.right.right
l = isCousin(root,a,b)
print(l)

