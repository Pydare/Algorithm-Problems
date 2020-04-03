class Node:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)

#count the number of nodes
def count(root):
    counter = 0
    q = [root]
    while q:
        temp = q.pop(0)
        counter += 1
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    return counter

def serialize(root,output):
    if not root:
        output.append('X')
        return
    output.append(root.val)
    serialize(root.left,output)
    serialize(root.right,output)
    return output
i = 0
def deserialize(source):
    global i 
    if source[i] == 'X':
        i += 1
        return None
    value = source[i]
    i += 1
    left = deserialize(source)
    right = deserialize(source)
    return Node(value,left,right)




# Driver Code 
if __name__ == '__main__': 
      
    # binary tree formation  
    root = Node(1,2,3)  
    root.left = Node(2,4,5)  
    root.right = Node(3,6,7)  
    root.left.left = Node(4,None,None)  
    root.left.right = Node(5,None,None)  
    root.right.left = Node(6,None,None)  
    root.right.right = Node(7,None,None)
    inorder(root)
    o = serialize(root,[])
    deserialize(o)
