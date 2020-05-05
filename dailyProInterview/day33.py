class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def minimumPathSum(root,s,l):
    if (not root):
        return
    s += root.val
    minimumPathSum(root.left,s,l)
    minimumPathSum(root.right,s,l)
    if (not root.left) and (not root.right):
        l.append(s)
    s -= root.val

    return (l)

root = Node(10)
root.left = Node(5)
root.left.left = Node(1)
root.left.right = Node(2)
root.right = Node(5)
root.right.right = Node(1)
root.right.right.left = Node(-1)

r = minimumPathSum(root,0,[])
print(r)