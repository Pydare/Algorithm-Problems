class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    q = [root]
    l = [] #store the root values
    while q:
        temp = q.pop()
        l.append(temp)
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
        if (not temp.left) and (not temp.right) and ()
