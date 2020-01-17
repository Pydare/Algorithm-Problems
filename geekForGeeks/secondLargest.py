class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorderList(p,arr):
    if p is None:
        return
    inorderList(p.left,arr)
    arr.append(p.data)
    inorderList(p.right,arr)

    return arr[len(arr)-2]

root = Node(10) 
root.left = Node(8) 
root.left.left = Node(7) 
root.left.left.left = Node(6) 
root.left.left.left.left = Node(5)

result = inorderList(root,[])
print(result)

# l = [1,2,3,4,5]
# print(l[-2])