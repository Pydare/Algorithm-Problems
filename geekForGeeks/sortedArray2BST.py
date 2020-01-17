class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2
    root = Node(arr[mid])

    root.left = sortedArrayToBST(arr[:mid])

    root.right = sortedArrayToBST(arr[mid+1:])
    return root

def preOrder(node):
    if not node:
        return
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

arr = [1,2,3,4,5,6,7]
root = sortedArrayToBST(arr)
print('preorder traversal of the BST ')
preOrder(root)