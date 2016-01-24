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
        def recurse (p, rightChild=False):
            if p==None: return
            if rightChild: print (", ", end="")
            print ("[", end="")
            recurse (p.left)
            print (p.data, end="")
            recurse (p.right, True)
            print ("]", end="")
            if not rightChild:
                if(p == self.root):
                    pass
                else:
                    print (", ", end="")
        print("In-Order: \t", end = "")
        recurse (self.root)
        print( )

    def preOrder (self):
        def recurse (p, rightChild=False):
            if p==None: return
            if p == self.root:
                pass
            else:
                print (", ", end="")
            print ("[", end="")
            print (p.data, end="")
            recurse (p.left)
            recurse (p.right, True)
            print ("]", end="")
        print("Pre-Order: \t", end = "")
        recurse (self.root)
        print( )

    def postOrder (self):
        def recurse (p, rightChild=False):
            if p==None: return
            print ("[", end="")
            recurse (p.left)
            recurse (p.right, True)
            print (p.data, end="")
            print ("]", end="")
            if p == self.root:
                pass
            else:
                print (", ", end="")
        print("Post-Order: \t", end = "")
        recurse (self.root)
        print( )

    def levelOrder (self):
        q = Queue()
        x = self.root
        test = False
        q.enqueue(BSTNode("["))
        if(x.left != None):
            q.enqueue(x.left)
        if(x.right != None):
            q.enqueue(x.right)
        line = "[" + str(x.data) + "], "
        while not(q.isEmpty()):
            x = q.dequeue()
            line += str(x.data)
            if test:
                if((x.left != None) or (x.right != None)):
                    q.enqueue(BSTNode("["))
                    test = False
            if(str(x.data) == "["):
                q.enqueue(BSTNode("]"))
                test = True
            if q.isEmpty():
                pass
            else:
                if(str(x.data) != "["):
                    if(str(q.front.data.data) == "]"):
                        pass
                    else:
                        line += ", "
            if(x.left != None):
                q.enqueue(x.left)
            if(x.right != None):
                q.enqueue(x.right)
        print ("Level-Order: \t" + "[" + line + "]", end="")
        print( )

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
