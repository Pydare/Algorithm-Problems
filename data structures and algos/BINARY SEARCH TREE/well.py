class Node:
    def __init__(self,value):
        self.value = value
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self):
        self.root = None
    def isempty(self):
        return self.root = None 
    def insert1(self,x):
        self.root = self._insert(self.root,x)
    def _insert(self,p,x):
        if p is None:
            p = Node(x)
        if x < p.value:
            p.lchild = _insert(p.lchild,x)
        elif x > p.value:
            p.rchild = _insert(p.rchild,x)
        else:
            print(x,' already present')
        return p
    def insert1(self,x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
            else:
                print(x,' already present in the tree')
                return
        temp = Node(x)
        if par == None:
            self.root = temp
        elif x < par.info:
            par.lchild = temp
        else:
            par.rchild = temp
    def search(self,x):
        return self._search(self.root,x) is not None
    def _search(self,p,x):
        if p is None:
            return None
        elif x < p.value:
            return _search(p.lchild,x)
        elif x > p.value:
            return _search(p.rchild,x)
        return p
    def delete1(self,x):
        p = self.root
        par = None
        while p is not None:
            if x == p.value:
                break
            par = p
            if x < p.info:
                p = p.lchild
            else:
                p = p.rchild
        if p == None:
            print(x,' not found')
            return
        #case c for 2 kids
        if p.lchild is not None and p.rchild is not None:
            ps = p
            s = p.rchild

            while s.lchild is not None:
                ps = s
                s = s.lchild
            p.info = s.info
            p = s
            par = ps
        if p.lchild is not None:
            ch = p.lchild
        else:
            ch = p.rchild
        if par == None:
            self.root = ch
        elif p == par.lchild:
            par.lchild = ch
        else:
            par.rchild = ch
