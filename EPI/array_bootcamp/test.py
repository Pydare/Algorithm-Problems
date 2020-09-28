d = {1:2,2:3,3:4,5:6}
#print(d)

def add_to_keys(d,x):
    res = []
    for k,v in d.items():
        res.append((k+x,v))

    d = {}
    for k,v in res:
        d[k] = v
    return d
res = add_to_keys(d,10)
#print(res)


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
def level_order(root):
    q = deque([root])
    temp = deque()
    
    while q:
        n = len(q)
        print(list(q))
        for _ in range(n):
            node = q.popleft()
            node.next = None if not q else q[0]
            temp.append(node)
        while temp:
            node = temp.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

res = level_order(root)
print(res)