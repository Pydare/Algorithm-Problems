class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def valuesAtHeight(root, height):
    if root == None:
        return
    if height == 1:
        return root.value
    if root.left != None and root.right != None:
        return valuesAtHeight(root.left,height-1), valuesAtHeight(root.right,height-1)
    if root.left == None and root.right != None:
        return valuesAtHeight(root.right, height-1)
    return valuesAtHeight(root.left, height-1)



r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.right = Node(7)

ans = valuesAtHeight(r,3)
print(ans)