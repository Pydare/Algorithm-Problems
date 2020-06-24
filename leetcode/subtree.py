class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def check(s_root,t_root):
    if not s_root and not t_root:
        return True
    if not s_root or not t_root:
        return False
   
    return s_root.val == t_root.val and check(s_root.left,t_root.left) and check(s_root.right,t_root.right)

def search(s_root,t_root):
    if not s_root:
        return False
    if s_root.val == t_root.val:
        return check(s_root,t_root)
    l = search(s_root.left,t_root)
    if l:
        return True
    r = search(s_root.right,t_root)
    if r:
        return True
    return False
    
s_root = Node(3)
s_root.left = Node(4)
s_root.right = Node(5)
s_root.left.left = Node(1)
s_root.left.right = Node(2)

t_root = Node(4)
t_root.left = Node(1)
t_root.right = Node(2)

ans = search(s_root, t_root)
print(ans)