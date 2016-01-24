
class Node:
    def __init__ (self, x, p):
        self.data = x
        self.next = p

class Queue:
    def __init__ (self):
        self.front = None
        self.back = None
        self.n = 0

    def size (self):
        return self.n

    def isEmpty(self):
        return self.n == 0

    def enqueue (self, x):
        p = Node (x, None)
        if self.isEmpty( ):
            self.front = p
        else:
            self.back.next = p
        self.back = p
        self.n += 1

    def dequeue (self):
        if self.isEmpty( ):
            raise KeyError ("Queue is empty.")
        x = self.front.data
        self.front = self.front.next
        if self.front == None:
            self.back == None
        self.n -= 1
        return x

class Multiple_Queues:
    def __init__ (self):
        self.Q = Queue( )

    def enqueue (self, qnum, item):
        self.Q.enqueue(Node(qnum, None))
        self.Q.enqueue(Node(item, None))
        
        

    def dequeue (self, qnum):
        test = 0
        y = 0
        self.Q.enqueue(Node(-1, None))
        x = self.Q.dequeue()
        while(x.data != -1):
            if(x.data == qnum and test == 0):
                y = self.Q.dequeue().data
                test +=1
            else:
                self.Q.enqueue(x)
                self.Q.enqueue(self.Q.dequeue())
            x = self.Q.dequeue()
        return y
                
def main( ):
    M = Multiple_Queues( )
    x = int (input ("Enter number of queues: "))
    y = int (input ("Enter number of items per queue: "))
    b = 1
    while b<=y:
        a = 0
        while a<x:
            M.enqueue (a, a+b*x)	# enqueue value (a+b*x) into queue number a
            a += 1
        b += 1

    a = 0
    while a<x:
        print ("Queue", a, ":", end=" ")
        b = 1
        while b<=y:
            print (M.dequeue (a), end=" ")
            b += 1
        a += 1
        print( )

if __name__ == '__main__':
    main( )
