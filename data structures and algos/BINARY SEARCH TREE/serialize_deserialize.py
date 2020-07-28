from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

class Codec:
    def __init__(self):
        self.data = " "
        self.root = None

    def serialize(self, root):
        h = self.height(root) 
        self.extend_tree(root,0,h)
        qu = deque()
        qu.append(root)

        while not qu:
            temp = qu.popleft()
            self.data += str(temp.val)
            self.data += ' '
            if temp.left:
                qu.append(temp.left)
            if temp.right:
                qu.append(temp.right)

        #removing both left and right spaces
        self.data = self.data.lstrip()
        self.data = self.data.rstrip()
        return self.data


    def height(self,root):
        if not root:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)

        if lheight > rheight:
            return 1 + lheight
        else:
            return 1 + rheight
    
    def extend_tree(self,root, curr, height):
        if not root or root == 'null':
            return 
        if not root.left and not root.right and curr < height:
            root.left = 'null'
            root.right = 'null'
        self.extend_tree(root.left,curr+1,height)
        self.extend_tree(root.right,curr+1,height)
       

    def deserialize(self, data):
        pass

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

codec = Codec()
res = codec.serialize(root)
print(res)

        