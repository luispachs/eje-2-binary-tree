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
            return None
    
        while n != None:
            if n._current == value:
                print(n._current)
                break
            print(n._current)
            n.search(n.left if value < n._current else n.right,value)
        return
    
    def delete(self,n,value:int|float):
        if n == None:
            return
        if value == n._current:
            if n.right == None and n.left == None:
                n = None
            if n.rigth == value:
                n.right == None
            if n.left == value:
                n.left == None
        else:
            n.delete(n.left if value < n._current else n.right,value)


    def showTwoChild(self,n):
        if n == None:
            return
        if n.left != None and n.right != None:
            print(n._current)
        n.showTwoChild(n.left)
        n.showTwoChild(n.right)