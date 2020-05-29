class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

def inorder(root):
    if not root:
        return
    if root.left:
        inorder(root.left)
    print(root.val, end=',')
    if root.right:
        inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(inorder(root))