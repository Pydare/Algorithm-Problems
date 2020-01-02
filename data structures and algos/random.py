l = [2,34,21,7,5,31,20,56]
def bubble(l):
    for i in range(len(l)):
        if l[i] > l[i+1]:


def reverse(self):
        p1 = self.start
        p2 = p1.next
        p1.next = None
        p1.prev = p2
        while p2.next is not None:
                p2.prev = p2.next