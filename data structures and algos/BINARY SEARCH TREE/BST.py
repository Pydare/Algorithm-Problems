class Node:
    def __init__(self,value):
        self.info = value
        self.lchild = None
        self.rchild = None

class BinarySearchTree: 
    def __init__(self):
        self.root = None
    def isempty(self,x):
        return self.root == None
    def insert(self,x):
        self.root = self._insert(self.root,x)
    def _insert(self,p,x):
        if p is None:
            p = Node(x)
        elif x < p.info:
            p.lchild = self._insert(p.lchild,x)
        elif x > p.info:
            p.rchild = self._insert(p.rchild,x)
        else:
            print(x,' already present in the tree')
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
                print(x + ' already present in the tree')
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
        if x < p.info:
            return self._search(p.lchild,x)
        if x > p.info:
            return self._search(p.rchild,x)
        return p
    def search1(self,x):
        p = self.root
        while p is not None:
            if x < p.info:
                p = p.lchild
            elif x > p.info:
                p = p.rchild
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
            print('Tree is empty dawg')
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.info
    def min2(self):
        if self.empty():
            print('Tree is still empty')
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
            print(x,' is not found')
            return
        #case c: 2 children 
        #find the inorder successor and it's parent
        #the inoder successor is the left most child in the right subtree

        if p.lchild is not None and p.rchild is not None:
            ps = p #the parent of p is now made p
            s = p.rchild #the right child of p for the inorder sucessor process

            while s.lchild is not None: #looking for left most child
                ps = s
                s = s.lchild
            p.info = s.info #copying the successor into node to be deleted
            p = s
            par = ps #previous parent of inorder successor turns to parent of last one to be delted
            
            
            '''trying to be consistent with the use of p and par incase 
            case A, B, or C occurs'''

            if p.lchild is not None:
                ch = p.lchild
            else p.rchild is not None:
                ch = p.rchild
            
            if par == None:
                self.root = ch
            elif p == par.lchild:
                par.lchild = ch
            else:
                par.rchild = ch

    def delete(self,x):
        self.root = self._delete(self.root,x)
    def _delete(self,p,x):
        if p is None:
            print(x,' not found')
            return p
        if x < p.info:
            p.lchild = self._delete(p.lchild,x)
        elif x > p.info:
            p.rchild = self._delete(p.rchild,x)
        else:
            #key to be deleted is found
            if p.lchild is not None and p.rchild is not None:
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild,s.info)
            else:
                if p.lchild is not None:
                    ch = p.lchild
                else:
                    ch = p.rchild
                p = ch
        return p


                
