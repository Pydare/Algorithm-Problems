from statistics import mode
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def most_freq_subtree_sum(root):
    #base case
    if not root:
        return 0
    l_value = most_freq_subtree_sum(root.left)
    r_value = most_freq_subtree_sum(root.right)

    node_sum = l_value+r_value+root.val
    l = []
    l.append(node_sum)

    return(l)
    

root = Node(3)
root.left = Node(1)
root.right = Node(-3)

r = most_freq_subtree_sum(root)
print(r)