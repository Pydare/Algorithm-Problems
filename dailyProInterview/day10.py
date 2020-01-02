class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
    p = root_node 
    if k < root_node:
        while k > p.value:
            p = p.left
        floor = p
        f = floor
        while k < f.value and f.value is not None:
            f = f.right
    elif k > root_node:
            #right subtree

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14)