class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None


def largest_diameter(root):
    max_diamter = [0]

    def dfs(root):
        if not root:
            return
        temp_diameter = height(root)
        if temp_diameter > max_diamter[0]:
            max_diamter[0] = temp_diameter
        dfs(root.left)
        dfs(root.right)

    dfs(root)
    return  max_diamter[0]

def height(root):
    if not root:
        return 0

    left = height(root.left)
    right = height(root.right)

    if left > right:
        return 1 + left
    else:
        return 1 + right

def diameter_optimal(root, diameter):
    if not root:
        return 0, diameter

    lheight, diameter = diameter_optimal(root.left,diameter)
    rheight, diameter = diameter_optimal(root.right,diameter)

    max_diameter = lheight + rheight + 1

    diameter = max(diameter, max_diameter)

    print(diameter,max_diameter)

    return max(lheight,rheight)+1, diameter




root = Node(1)
root.left = Node(2)
root.left.right = Node(4)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

diameter = 0
res = diameter_optimal(root,diameter)[1]
print(res)