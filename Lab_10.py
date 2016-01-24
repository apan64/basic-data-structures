
import operator

class Heap:
    def __init__ (self, comparator):
        self.isOrdered = comparator
        self.array = list( )
        self.n = 0

    def __repr__ (self):
        return self.array.__repr__ ( )

    def insert (self, x):
        self.array.append(x)
        self.n += 1
        q = int(len(self.array) - 1)
        p = int((q - 1) / 2)
        while(not self.isOrdered(self.array[p], self.array[q])):
            temp = self.array[q]
            self.array[q] = self.array[p]
            self.array[p] = temp
            q = int(p)
            if(((q - 1) / 2) > (-1)):
                p = int((q - 1) / 2)
            else:
                break
        

    def remove (self):
        if self.n==0:
            return None
        self.n -= 1
        x = self.array[0]
        y = self.array.pop (self.n)
        if self.n==0:
            return x
        p = 0
        left = 1
        right = 2
        while (left<self.n and not self.isOrdered (y, self.array[left])) \
          or (right<self.n and not self.isOrdered (y, self.array[right])):
            c = left
            if right<self.n and not self.isOrdered (self.array[left], self.array[right]):
                c = right
            self.array[p] = self.array[c]
            p = c
            left = 2*p+1
            right = left+1
        self.array[p] = y
        return x

class MinHeap (Heap):
    def __init__ (self):
        super( ).__init__ (operator.le)		# Less than or Equal operator (<=)

class MaxHeap (Heap):
    def __init__ (self):
        super( ).__init__ (operator.ge) 	# Greater than or Equal operator (>=)

def main( ):
    L = eval (input ("Enter a Python list: "))
    n = len(L)
    H1 = MinHeap( )
    L1 = [None]*n
    for x in L:
        H1.insert (x)
        print ("Insert " + str(x) + ":", end="\t")
        print (H1)
    for k in range(n):
        x = H1.remove( )
        print ("Remove " + str(x) + ":", end="\t")
        print (H1)
        L1[k] = x
    print ("Sorted list: ", end="\t")
    print (L1)
    H2 = MaxHeap( )
    L2 = [None]*n
    for x in L:
        H2.insert (x)
        print ("Insert " + str(x) + ":", end="\t")
        print (H2)
    for k in reversed (range(n)):
        x = H2.remove( )
        print ("Remove " + str(x) + ":", end="\t")
        print (H2)
        L2[k] = x
    print ("Sorted list: ", end="\t")
    print (L2)

if __name__ == '__main__':
    main( )
