class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def kthsmallest(root,k):
    q = []
    while True:
        while root:
            q.append(root)
            root = root.left
        root = q.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right
        
