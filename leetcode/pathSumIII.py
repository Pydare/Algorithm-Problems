from collections import Counter

class Node:
    def __init__(self,val):
        self.val = val
        self.left = self.right = None


def pathSum(root, sum: int):
        
    count = [0]
    def pathSumUtil(root,sum,d,cumsum):
        if not root:
            return 
        cumsum += root.val
        if d.get(cumsum,None) is None:
            d[cumsum] = 1
        else:
            d[cumsum] += 1
        if d.get(cumsum-sum,None)is not None:
            count[0] += d[cumsum-sum]
        #print(cumsum, end=' ')
        #print(d)
        pathSumUtil(root.left,sum,d,cumsum)
        pathSumUtil(root.right,sum,d,cumsum)
        
        #deleting instances of list's values when going back up
        if d[cumsum] == 1:
            del d[cumsum]
        elif d[cumsum] > 1:
            d[cumsum] -= 1
        cumsum -= root.val
    pathSumUtil(root,sum,{0:1},0)   
    return count[0]

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.left = Node(5)
root.right.right.right = Node(1)

r = (pathSum(root,22))
print(r)


