class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)
def helper_count(head):
    count = 0
    p = head
    while p.next is not None:
        count += 1
        p = p.next
    return count
def remove_kth_from_ll(head,k):
    tracker = 0
    total_count = helper_count(head)
    pause = total_count - k
    p = head
    while p is not None:
        tracker += 1
        if pause == 0:
            head == p.next.next
        elif tracker == pause:
            p = p.next.next
        elif tracker == pause and pause == total_count-1:
            p.next = None
        else:
            p = p.next
    return head
    