# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from queue import PriorityQueue

def mergeKLists(lists):
    
    if not lists:
        return None
    
    dummy = point = ListNode(0)
    q = PriorityQueue()
    i = 0
    
    for l in lists:
        if l:
            q.put((l.val, i, l))
            i += 1
            
    while not q.empty():
        val, _, node = q.get()
        point.next = node
        point = point.next  # moving pointer for new array
        node = node.next  # i'm moving this based on individual lists in the original array
        if node:
            q.put((node.val, i, node))
            i += 1
            
    return dummy.next
        