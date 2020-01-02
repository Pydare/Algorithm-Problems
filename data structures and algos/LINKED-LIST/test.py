class Node:
    def __init__(self,value):
        self.value = value
        self.link = None

class CircularLL:
    def __init__(self):
        self.last = None
    
    def concatenate(self,list2):
        if self.last is None:
            self.last = list2.last
            return
        if list2.last is None:
            return
        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last