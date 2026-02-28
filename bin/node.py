class node:
    left:int|float|None
    right:int|float|None
    _current:int|float|None
    def __init__(self,current:int|float|None = None):
        self._current = current
        self.left = None
        self.right = None


    def add(self,value:int|float):
        if value < self._current:
            if self.left == None:
                self.left = node(value)
            else:
                self.left.add(value)
        elif value > self._current:
            if self.right == None:
                self.right = node(value)
            else:
                self.right.add(value)

    def inorder(self,n):
        if n == None:
            return None
        n.inorder(n.left)
        print(n._current)
        n.inorder(n.right)

    def preorder(self,n):
        if n == None:
            return None
        print(n._current)
        n.preorder(n.left)
        n.preorder(n.right)

    def postorder(self,n):
        if n == None:
            return None
        n.postorder(n.left)
        n.postorder(n.right)
        print(n._current)
    
    def search(self,n,value:int|float):
        if n == None:
            return False
        print(n._current) 
        if value == n._current:
            return True
        else:
            return n.search(n.left if value < n._current else n.right,value)
    
    def delete(self,n,value:int|float):
        if n == None:
            return None
        if value == n._current:
            if n.right == None and n.left == None:
                n = None
                return
            if n.right != None and n.right == value:
                n.right = None
                return
            if n.left != None and n.left == value:
                n.left = None
                return
        else:
            return n.delete(n.left if value < n._current else n.right,value)


    def showTwoChild(self,n):
        if n == None:
            return
        if n.left != None and n.right != None:
            print(n._current)
        n.showTwoChild(n.left)
        n.showTwoChild(n.right)
    
    def showOneChild(self,n):
        if n == None:
            return None
        
        if(n.left != None and n.right == None) or (n.left == None and n.right != None): 
            print(n._current)
        n.showOneChild(n.left)
        n.showOneChild(n.right)


    def sumChild(self,n):
        if n == None:
            return 0
        print((n.left._current if n.left != None else 0) + (n.right._current if n.right != None else 0))
        n.sumChild(n.left)
        n.sumChild(n.right)