
class Node:
    def __init__ (self, x, q):
        self.data = x
        self.next = q

class Stack:
    def __init__ (self):
        self.top = None

    def isEmpty (self):
        return self.top == None

    def push (self, x):
        self.top = Node (x, self.top)

    def pop (self):
        if self.isEmpty( ):
            raise KeyError ("Stack is empty.")
        x = self.top.data
        self.top = self.top.next
        return x

class List:
    def __init__ (self):
        self.head = None

    def build_list (self):
        str = input ("Enter strings separated by blanks: ")
        for x in str.split (" "):
            if self.head == None:
                self.head = Node (x, None)
                curr = self.head
            else:
                curr.next = Node (x, None)
                curr = curr.next

    def display (self):
        curr = self.head
        while curr != None:
            print (curr.data, end=" ")
            curr = curr.next
        print( )

    def reverse_display_1 (self):
        st = Stack()
        curr = self.head
        while curr != None:
            st.push(curr.data)
            curr = curr.next
        while (not(st.isEmpty())):
            print(st.pop(), end = " ")
        print( )
            
    def recur(self, q):
        if q.next != None:
            self.recur(q.next)
        print(q.data, end = " ")
        
    
    def reverse_display_2 (self):
        self.recur(self.head)
        print( )

    
    def reverse_display_3 (self):
        w = self.head
        curr = self.head
        head = self.head
        head = head.next
        curr.next = None
        while head != None:
            curr = head
            head = head.next
            curr.next = w
            w = curr
        head = curr.next
        while curr != None:
            print (curr.data, end=" ")
            curr = curr.next
        print( )
        curr = w
        curr.next = None
        while head != None:
            curr = head
            head = head.next
            curr.next = w
            w = curr
        

def main( ):
    L = List( )
    L.build_list( )
    print ("Forward: ", end="\t")
    L.display( )
    print ("Backward: ", end="\t")
    L.reverse_display_1( )
    print ("Backward: ", end="\t")
    L.reverse_display_2( )
    print ("Backward: ", end="\t")
    L.reverse_display_3( )
    print ("Forward: ", end="\t")
    L.display( )

if __name__ == '__main__':
    main( )
