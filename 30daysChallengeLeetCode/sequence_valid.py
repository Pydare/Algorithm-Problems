class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

        
def existPath(root,arr):

    n = len(arr)
    if not root:
        return 0

    def existPathUtil(root,arr,n,index):
        # if root is null or reached (passed) the end of the array
        if not root or index == n:
            return False
        # if current node is leaf
        if not root.left and not root.right:
            if root.val == arr[index] and index == n-1:
                return True
            return False

        # if current node is equal to arr[idx], till this levle path has been matched; remaining path can be either left or right subtree
        flag = (index<n) and (root.val == arr[index]) and (existPathUtil(root.left,arr,n,index+1)) or (existPathUtil(root.right,arr,n,index+1))
        return flag

    return existPathUtil(root,arr,n,0)


root = Node(0)
root.left = Node(1)
root.left.left = Node(0)
root.left.left.right = Node(1)
root.left.right = Node(1)
root.left.right.left = Node(0)
root.left.right.right = Node(0)
root.right = Node(0)
root.right.left = Node(0)

r = existPath(root,[0,1,0,1])
print(r)

