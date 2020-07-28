class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def mirror(root):
    if not root:
        return
    
    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left
