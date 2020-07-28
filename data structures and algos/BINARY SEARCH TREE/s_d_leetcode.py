from collections import deque
class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None


def serialize(root):

    def rserialize(root,string):
        #base case
        if not root:
            string += 'None,'
        else:
            string += str(root.val) + ','
            string = rserialize(root.left,string)
            string = rserialize(root.right,string)
        return string

    return rserialize(root,'')

def deserialize(data):

    def rdeserialize(l):
        if l[0] == 'None':
            l.popleft()
            return None
        root = Node(l[0])
        root.left = rdeserialize(l)
        root.right = rdeserialize(l)
        return root 

    data_list = data.split(',')
    data_list = deque(data_list)
    root = rdeserialize(data_list)
    return root 
