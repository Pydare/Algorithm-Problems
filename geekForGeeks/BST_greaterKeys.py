class Node:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

def addGreaterUtil(root,sum_ptr):
    if root == None:
        return
    addGreaterUtil(root.right,sum_ptr)

    sum_ptr[0] = sum_ptr[0] + root.key

    root.key = sum_ptr[0]

    addGreaterUtil(root.left,sum_ptr)

def addGreater(root):
    Sum = [0]
    addGreaterUtil(root,Sum)

def printInorder(node):
    if node == None:
        return
    printInorder(node.left)
    print(node.key,end=' ')
    printInorder(node.right)


if __name__ == '__main__': 
      
    # Create following BST  
    #         5  
    #     / \  
    #     2     13  
    root = Node(5)  
    root.left = Node(2)  
    root.right = Node(13)  
  
    print("Inorder traversal of the given tree")  
    printInorder(root) 
  
    addGreater(root)  
    print() 
    print("Inorder traversal of the modified tree")  
    printInorder(root)