class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def kLast(head,k):
    def count(head):
        p = head
        count = 1
        while p.next is not None:
            p = p.next
            count += 1
        return count

    total = count(head)
    target = total - (k-1) #kth to the last is the (k-1) last 
    c = 1
    p = head
    while p.next is not None:
        if c == target:
            return p
        p = p.next
        count += 1
    return p 