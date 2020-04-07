class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def delelteNode(root,x):
    #first step is looking for x
    if root.val == x:
        root = None
        return root
    p = root
    while p is not None:
        if x < p.val:
            p = p.left
        elif x > p.val:
            p = p.right
        else:
            print(x, ' has been found')
    
