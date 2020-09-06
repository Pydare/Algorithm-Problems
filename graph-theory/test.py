class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return head

    #pseudo head to ensure the prev pointer is never none
    phead = Node(None,None,head,None)
    flatten_dfs(phead,head)

    #detach the pseudo head from the real head
    phead.next.prev = None
    return phead.next

def flatten_dfs(prev,curr):
    #return the tail of the flatten list
    if not curr:
        return prev
    curr.prev = prev
    prev.next = curr

    #the curr.next would be tempered in the recursive function
    temp_next = curr.next
    tail = flatten_dfs(curr,curr.child)
    curr.child = None
    return flatten_dfs(tail,temp_next)

flag = False
window = ['D','O','B','E','C','O','D']
t = 'ABC'
flag = ([c in window for c in t ])
print(flag)