from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def isempty(self):
        return self.root = NotImplemented
    def display():
        self._display(self.root)
        print()
    def _display(self,p):
        if p is None:
            return
        _display(self,p.left)
        print(p.value,' ',end='')
        _display(self,p.right)
    def preorder(self):
        self._preorder(self.root)
        print()
    def _preorder(self,p):
        if p is None:
            return
        print(p.value,' ',end='')
        self._preorder(p.left)
        self._preorder(p.right)
    def levelorder(self):
        if self.root is None:
            return
        q = []
        q.append(self.root)

        while len(q) != 0:
            p = q.pop(0)
            print(p.info, ' ', end='')
            if p.left is not None:
                q.append(p.left)
            if p.right is not None:
                q.append(p.right)   
    def height(self):
        return self._height(self.root)
    def _height(self,p):
        if p is None:
            return 0
        hl = self._height(p.left)
        hr = self._height(p.right)

        if hl > hr:
            return hl +1
        else:
            return hr + 1
    def invert_tree(self):
        self.root =  self._invert(self.root)
    def __invert(self,p):
        if l.value or r.value is None:
            return
        l = self.__invert(p.left)
        r = self.__invert(p.right)

        l.value, r.value = r.value, l.value
        return p

