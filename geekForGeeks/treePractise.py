class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.nxt = None

# function to find left most node in a tree
def leftMostNode(node):
    while (node != None and node.left != None):
        node = node.left
    return node

#function to find right most node in a tree
def rightMostNode(node):
    while (node != None and node.right != None):
        node = node.right
    return node
    
# recursive function to find the inorder successor when the right child of node x is None
def findInorderRecur(root,x):
    if not root:
        return None
    if (root == x or (findInorderRecur(root.left,x)) or (findInorderRecur(root.right,x)) ):
        if findInorderRecur(root.right,x): 
            temp = findInorderRecur(root.right,x)
        else:
            temp = findInorderRecur(root.left,x)
        if temp:
            if root.left == temp:
                print("Inorder successor of ", x.val, end = '')
                print('is, ', root.val)
                return None
        return root
    return None

# function to find inorder successor of a node
def inorderSuccessor(root,x):
    # case 1: if right child is not None
    if x.right != None:
        inorderSucc = leftMostNode(x.right)
        print('Inorder successor of ',x.val,'is ',end=' ')
        print(inorderSucc.val)

    #case 2: if right child is None
    if x.right == None:
        f = 0
        rightMost = rightMostNode(root)

        # case 3: if x is the right most node
        if rightMost == x:
            print('No inorder successor')
        else:
            findInorderRecur(root,x)



   



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)






    

    


