class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None


def addChildSum(root):
    if not root:
        return

    addChildSum(root.left)
    addChildSum(root.right)

    finalSum = root.val
    if root.left:
        finalSum += root.left.val
    if root.right:
        finalSum += root.right.val

    root.val = finalSum