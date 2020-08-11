class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
12, 11, 13, 5, 6, 7
12 11 13
12  11  13
"""


def mergeKsorted(lists):
    if not lists:
        return
    if len(lists)==1:
        return lists[0]
    
    mid = len(lists)//2
    l = mergeKsorted(lists[:mid])
    r = mergeKsorted(lists[mid:])
    
    return merged(l,r)

def merged(l,r):
    dummy = curr = ListNode(0)

    while l and r:
        if l.val < r.val:
            curr.next = ListNode(l.val)
            l = l.next
            curr = curr.next
        else:
            curr.next = ListNode(r.val)
            r = r.next
            curr = curr.next
    curr.next = l or r
    return dummy.next


"""merge k sorted lists
[1->4->5, 1->3->4, 2->6 ]
"""