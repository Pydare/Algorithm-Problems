from collections import deque

class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def isempty(self):
        return self.root == None
    def display(self):
        self._display(self.root, 0)
        print()
    def _display(self, p ,level):
        if p is None:
            return
        self._display(p.rchild, level+1)
        print()

        for i in range(level):
            print(' ', end='')
        print(p.info)
        self._display(p.lchild, level+1)
    def preorder(self):
        self._preorder(self.root)
        print()
    def _preorder(self,p):
        if p is None:
            return
        print(p.info, ' ', end='')
        self._preorder(p.lchild)
        self._preorder(p.rchild)
    def inorder(self):
        self._inorder(self.root)
        print()
    def _inorder(self, p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info, ' ', end='')
        self._inorder(p.rchild)
    def postorder(self):
        self._postorder(self.root)
        print()
    def _postorder(self, p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info, ' ', end='')