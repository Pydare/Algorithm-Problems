class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=' ')
    inorder(root.right)
    

def inorder_list(root,arr):
    if root is None:
        return
    inorder_list(root.left,arr)
    arr.append(root.val)
    inorder_list(root.right,arr)
    arr.append(0)
    change_list(arr)
    return arr

def change_list(arr):
    m = arr
    for i in range(1,len(arr)-1):
        arr[i] = m[i-1] + m[i+1]

def rearrange(root,arr):
    if root is None:
        return
    rearrange(root.left,arr)
    root.val = arr[0]
    arr.pop(0)
    rearrange(root.right,arr)

root = Node(10)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(8)
root.right.right = Node(1)

inorder(root)
arr = inorder_list(root,[0])
rearrange(root,arr)
print()
inorder(root)