class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):
    p = head
    prev = None
    while p is not None:
        next = p.next
        p.next = prev
        prev = p
        p = next
    head = prev

  # Recursive Solution      
  def reverseRecursively(self, head):
    if prev.next is None:
        head = prev
    prev = None
    p = head
    next_ = p.next
    reverseRecursively(head.next)