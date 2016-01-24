import math

class AdjMatrixGraph:
    def __init__ (self, n):
        self.n = n
        self.array = []
        for x in range(n):
            q = []
            for y in range(n):
                q.append(int(0))
            self.array.append(q)

    def display (self):
        for x in range (self.n):
            for y in range (self.n):
                print ("{0:2}".format(self.array[x][y]), end=" ")
            print( )
        print( )

    def insert (self, x, y, w):
        self.array[x][y] = int(w)

    def floyd (self):
        for i in range(0, self.n):
            for r in range(0, self.n):
                for c in range(0, self.n):
                    self.array[r][c] = min(self.array[r][c], self.array[r][i] + self.array[i][c])

def main( ):
    n = eval(input("Enter number of vertices: "))
    G = AdjMatrixGraph(n)
    G.display( )
    k = math.ceil(math.sqrt(n))
    for x in range(n):
        for y in range(n):
            if x!=y:
                weight = (x%k-y%k)**2 + (x//k-y//k)**2 + 1
                G.insert(x, y, weight)
    G.display( )
    G.floyd( )
    G.display( )

if __name__ == '__main__':
    main( )
