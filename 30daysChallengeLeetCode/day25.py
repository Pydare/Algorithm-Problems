class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def pathSum(root,summ, key):
    #base case
    if not root:
        return
    summ += root.val
    if summ == key:
        return True
    else:
        return False
    
    print(summ,end=' ')
    return pathSum(root.left,summ,key) or pathSum(root.right,summ, key)
    #summ -= root.val
    
    
    

root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
ans = pathSum(root,0,50)
print(ans)