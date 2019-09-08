class Node:
    def __init__(self, value):
        self.info = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def isempty(self):
        return self.root == None
    def insert(self, x):
        self.root = self._insert(self.root,x)
    def _insert(self,p,x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild,x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild, x)
        else:
            print(x, ' already present in  the tree')
        return p
    def insert1(self, x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
            else:
                print(x + ' already pressent in the tree')
                return
        temp = Node(x)
        if par == None:
            self.root = temp
        elif x < par.info:
            par.lchild = temp
        else:
            par.rchild = temp
    def search(self,x):
        return self._search(self.root, x) is not None
    def _search(self,p,x):
        if p is None:
            return None #key not found
        if x < p.info:
            return self._search(p.lchild, x) #search in left subtre
        if x > p.info:
            return self._search(p.rchild, x) #search in right subtree
        return p #key found
    def search1(self,x):
        p = self.root
        while p is not None:
            if x < p.info:
                p = p.lchild #move to left child
            elif x > p.info:
                p = p.rchild #move to right child
            else:
                return True
        return False
    def min1(self):
        if self.isempty():
            print('Tree is empty')
        p = self.root
        while p.lchild is not None:
            p = p.lchild
        return p.info
    def max1(self):
        if self.isempty():
            print('Tree is empty')
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.info
    def min2(self):
        if self.isempty():
            print('Tree is empty')
        return self._min(self.root).info
    def _min(self,p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)
    def max2(self):
        if self.isempty():
            print('Tree is empty')
        return self._max(self.root).info
    def _max(self,p):
        if p.rchild is None:
            return p
        return self._max(p.rchild)

    def delete1(self,x):
        p = self.root
        par = None
        while p is not None:
            if x == p.info:
                break
            par = p 
            if x < p.info:
                p = p.lchild
            else:
                p = p.rchild
        if p == None:
            print(x, ' not found')
            return
        #case c: 2 children
        #find inorder successor and its parent
        if p.lchild is not None and p.rchild is not None:
            ps = p
            s = p.rchild

            while s.lchild is not None:
                ps = s
                s = s.lchild
            p.info = s.info
            p = s
            par = ps
        #case b and case a: 1 or no child
        if p.lchild is not None: #node to be deleted has left child
            ch = p.lchild
        else:       #node to be deleted has right child or no child
            ch = p.rchild
        if par == None: #node to be deleted is root node
            self.root = ch
        elif p == par.lchild:  #node is left child of its parent
              par.lchild = ch
        else:
            par.rchild = ch
        
    def delete(self,x):
        self.root = self._delete(self.root,x)
    def _delete(self,p,x):
        if p is None:
            print(x,' not found')
            return p
        if x < p.info: #delete from left subtree
            p.lchild = self._delete(p.lchild,x)
        elif x > p.info: #delete from right subtree
            p.rchild = self._delete(p.rchild,x)
        else:
            #key to be deleted is found
            if p.lchild is not None and p.rchild is not None:
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild,s.info)
            else: #1 child or no child
                if p.lchild is not None:
                    ch = p.lchild
                else:
                    ch = p.rchild
                p = ch
        return p