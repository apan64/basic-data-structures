import math
import sys

class AdjMatrixGraph:
    def __init__ (self):
        self.n = 0
        self.array = []
        self.arraynames = []

    def display (self):
        for x in range (self.n):
            for y in range (self.n):
                print ("{0:2}".format(self.array[x][y]), end=" ")
            print( )
        print( )

    def insert (self, x, y, w):
        self.array[x][y] = int(w)
        
    def update(self):
        if len(self.array) < self.n:
            x = self.n - len(self.array)
            for q in range(0, x):
                for row in self.array:
                    row.append(int(0))
            for q in range(0,x):
                new = []
                for y in range(self.n):
                    new.append(int(0))
                self.array.append(new)

    def read(self, file):
        reader = open(file, "r")
        for line in reader:
            q = str(line).split()
            try:
                x = self.arraynames.index(q[0])
            except:
                x = self.n
                self.n += 1
                self.arraynames.append(q[0])
            try:
                y = self.arraynames.index(q[2])
            except:
                y = self.n
                self.n += 1
                self.arraynames.append(q[2])
            self.update()
            self.array[x][y] = (int(q[1]) - int(q[3]))
            self.array[y][x] = (int(q[3]) - int(q[1]))
        

def main():
    graph = AdjMatrixGraph()
    graph.read(input("Filename? "))
    graph.display()













            
