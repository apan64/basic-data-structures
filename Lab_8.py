
class QNode:
    def __init__ (self, x, p=None):
        self.data = x
        self.next = p

class Queue:
    def __init__ (self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return self.front == None

    def enqueue (self, x):
        p = QNode (x)
        if self.isEmpty( ):
            self.front = p
        else:
            self.back.next = p
        self.back = p

    def dequeue (self):
        if self.isEmpty( ):
            raise KeyError ("Queue is empty.")
        x = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.back == None
        return x

class BSTNode:
    def __init__ (self, x, L=None, R=None):
        self.data = x
        self.left = L
        self.right = R

class BST:
    def __init__ (self):
        self.root = None

    def insert (self, x):
        def recurse (p):
            if x<p.data:
                if p.left==None:
                    p.left = BSTNode (x)
                else:
                    recurse (p.left)
            else:
                if p.right==None:
                    p.right = BSTNode (x)
                else:
                    recurse (p.right)
        # body of insert method
        if self.root==None:
            self.root = BSTNode(x)
        else:
            recurse (self.root)

    def inOrder (self):
        # Complete this method.
        line = ""
        print ("InOrder:    ", self.inOrderHelper(self.root, line), end="")
        print( )

    def inOrderHelper(self, x, line):
        if x.left != None:
            line += self.inOrderHelper(x.left, line)
        line += str(x.data)
        line += " "
        if x.right != None:
            line += self.inOrderHelper(x.right, "")
        return line

    def preOrder (self):
        # Complete this method.
        line = ""
        print ("PreOrder:   ", self.preOrderHelper(self.root, line), end="")
        print( )

    def preOrderHelper(self, x, line):
        line += str(x.data)
        line += " "
        if x.left != None:
            line += self.preOrderHelper(x.left, "")
        if x.right != None:
            line += self.preOrderHelper(x.right, "")
        return line

    def postOrder (self):
        # Complete this method.
        line = ""
        print ("PostOrder:  ", self.postOrderHelper(self.root, line), end="")
        print( )

    def postOrderHelper(self, x, line):
        if x.left != None:
            line += self.postOrderHelper(x.left, "")
        if x.right != None:
            line += self.postOrderHelper(x.right, "")
        line += str(x.data)
        line += " "
        return line

    def levelOrder (self):
        # Complete this method.
        q = Queue()
        x = self.root
        q.enqueue(x.left)
        q.enqueue(x.right)
        line = str(x.data) + " "
        while not(q.isEmpty()):
            x = q.dequeue()
            line += str(x.data) + " "
            if(x.left != None):
                q.enqueue(x.left)
            if(x.right != None):
                q.enqueue(x.right)
        print ("LevelOrder: ", line, end="")
        print( )

def main( ):
    T = BST( )
    L = eval (input ("Enter a Python list: "))
    for x in L:
        T.insert (x)
    T.inOrder( )
    T.preOrder( )
    T.postOrder( )
    T.levelOrder( )

if __name__ == '__main__':
    main( )
