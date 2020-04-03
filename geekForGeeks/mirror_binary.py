class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def mirrorImage(node):
    if node is None:
        return
    mirrorImage(node.left)
    mirrorImage(node.right)
    temp = node.left
    node.right = node.left
    node.left = temp

def insert(node,x):
    p = node
    while p.left and p.right is not None:
        if x > p.value:
            p = p.right
        elif x < p.value:
            p = p.left
    if x > p.value:
        p.right = Node(x)
    elif x < p.value:
        p.left = Node(x)


def inOrder(node) : 
    if (node == None):  
        return     
    inOrder(node.left)  
    print(node.value, end = " ")  
    inOrder(node.right)

# Driver code  
if __name__ =="__main__":  
  
    root = Node(1)  
    root.left = Node(2)  
    root.right = Node(3)  
    root.left.left = Node(4)  
    root.left.right = Node(5) 
    insert(root,6) 
  
    """ Print inorder traversal of 
        the input tree """
    print("Inorder traversal of the",  
               "constructed tree is")  
    inOrder(root)  
      
    """ Convert tree to its mirror """
    # mirrorImage(root)  
  
    # """ Print inorder traversal of  
    #     the mirror tree """
    # print("\nInorder traversal of",  
    #           "the mirror treeis ")  
    # inOrder(root)