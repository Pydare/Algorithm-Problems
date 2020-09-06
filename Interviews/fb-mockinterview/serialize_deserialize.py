class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

from collections import deque
def serialize(root):
    res = []
    q = deque([root])

    if not root:
        return ''

    while q:
        node = q.popleft()

        if node:
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        else:
            res.append('null')
    return ','.join(res)

def deserialize(word):
    word = word.split(',')
    
    if  len(word) == 0:
        return None
    
    q = deque([Node(word[0])])
    i = 1
    while q:
        node = q.popleft()
        
        if word[i] != 'null':
            node.left = Node(word[i])
            q.append(node.left)
        
        i += 1

        if word[i] != 'null':
            node.right = Node(word[i])
            q.append(node.right)
        i += 1
    return root

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

            left, idx = decoder(idx+1)
            right, idx = decoder(idx+1)

            root.left = left
            root.right = right
        else:
            root = None
        return root, idx

    return decoder(0)[0]  


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

ans = serialize2(root)
print(ans)