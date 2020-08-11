class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def push(self,element,node=None):
        if node is None:
            node = self.root

        if self.root is None:
            self.root = Node(element)
        
        else:
            if element < node.data:
                if node.left is not None:
                    self.push(element, node.left)
                else:
                    node.left = Node(element)
            else:
                if node.right is not None:
                    self.push(element,node.right)
                else:
                    node.right = Node(element)

    def preorder(self,root):
        if not root:
            return
        print(root.data, ' ', end='')
        self.preorder(root.left)
        self.preorder(root.right)
    
    def __str__(self):
        self.preorder(self.root)
        return "\n"

bt = BinaryTree()
bt.push(1)
bt.push(2)
bt.push(3)
bt.push(4)
bt.push(5)
print(bt)

from collections import deque
def serialize(root):

    if not root:
        return ''

    res = []

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        if node:
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            res.append('null')

    return ','.join(res)

def deserialize(data):

    if len(data) == 0:
        return None

    data = data.split(',')

    q = deque()
    root = Node(data[0])
    q.append(root)
    idx = 1

    while q:
        node = q.popleft()

        if data[idx] != 'null':
            node.left = Node(data[idx])
            q.append(node.left)

        idx += 1

        if data[idx] != 'null':
            node.right = Node(data[idx])
            q.append(node.right)

        idx += 1
    return root

#DFS
def serialize2(root):
    if not root:
        return ""

    data = []

    def helper(root):

        if not root:
            data.append('null')
            return
        data.append(str(root.val))
        helper(root.left)
        helper(root.right)
    
    helper(root)
    return ','.join(data)

def deserialize2(data):
    if len(data) == 0:
        return None

    data = data.split(',')

    def decoder(idx):
        if data[idx] != 'null':
            root = Node(data[idx])

            left, idx = decoder(idx + 1)
            right, idx = decoder(idx + 1)

            root.left = left
            root.right = right
        else:
            root = None
        return root, idx
    return decoder(0)[0]