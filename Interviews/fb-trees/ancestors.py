class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None

"""
           1
        2      3
      4   5  6    7
    8   9
      10 11

    4 and 7 ---> 1
    10 and 4 ---> 4 (if a node is allowed to be a descendant of itself)
    1 and any other node ---> 1

    Edge case: if the second node comes after the first, return the first node
    else: keep track of all nodes visited before coming across the first node (included)
Time complexity: O(n) Space complexity: O(n)
"""

def search(root,p,q):

    def helper(root,p,q):
        if not root:
            return None
        if root.val==p or root.val==q:
            return root

        left = helper(root.left,p,q)
        right = helper(root.right,p,q)

        if left and right:
            return root
        else:
            return left if left else right

    return helper(root,p,q)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.left.right.left = Node(10)
root.left.left.right.right = Node(11)
root.right.left = Node(6)
root.right.right = Node(7)

ans = search(root,8,9)
print(ans.val)
