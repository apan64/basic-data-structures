
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

    def display (self):		# parenthesized inorder traversal
        def recurse (p, rightChild=False):
            if p==None: return
            if rightChild: print (" ", end="")
            print ("(", end="")
            recurse (p.left)
            print (p.data, end="")
            recurse (p.right, True)
            print (")", end="")
            if not rightChild: print (" ", end="")
        recurse (self.root)
        print( )

    def remove (self, x):
        self.root = self.removeHelper(self.root, x)
            

    def removeHelper(self, n, x):
         if(n.data == x):
              return self.findNext(n)
         elif(n.data < x):
             if(n.right != None):
                  n.right = self.removeHelper(n.right,x)
         else:
             if(n.left != None):
                  n.left =  self.removeHelper(n.left,x)
         return n

    def findNext(self,n):
        pointer = n
        if(n.right == None):
             n = n.left
        elif(n.left == None):
              n = n.right
        else: 
              pointer = n.right
              pointer2 = n
              while(pointer.left !=  None):
                    pointer2 = pointer
                    pointer = pointer.left
              n.data = pointer.data
              if(pointer2 == n):
                   pointer2.right = pointer.right
              else:
                   pointer2.left = pointer.right
        return n

def main( ):
    T = BST( )
    L = eval (input ("Enter a Python list: "))
    for x in L:
        T.insert (x)
    print ("Start tree: ", end="")
    T.display( )
    for x in L:
        T.remove (x)
        print ("Removing " + str(x) + ": ", end="")
        T.display( )

if __name__ == '__main__':
    main( )
