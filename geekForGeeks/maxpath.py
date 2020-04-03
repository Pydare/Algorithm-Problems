class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


def returnPaths(root):
    l = []
    m = []
    ans = paths(root,l,m)
    return ans

def paths(root,l,m):
    if root is None:
        return
    l.append(root.val)
    if root.left is None and root.right is None:
        m.append(l)
    if root.left:
        paths(root.left,l,m)
    if root.right:
        paths(root.right,l,m)
    l.pop()
    return m




root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
ans =  returnPaths(root)
print(ans)
