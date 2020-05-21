class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

left = [0]
def sumUtils(root,parent):
    #base case
    if not root:
        return          
    if not root.left and not root.right:
        if parent.left == root:
            left[0] += root.val                    
    sumUtils(root.left, root)
    sumUtils(root.right, root)
    return left[0]



root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(sumUtils(root,root))
