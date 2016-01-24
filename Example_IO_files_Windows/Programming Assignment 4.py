import math
import sys
import copy

class Games:
    def __init__ (self):
        self.games = []
    def add(self, x):
        self.games.append(x)
    def size(self):
        return len(self.games)
    def avg(self):
        if self.size() == 0:
            return 0
        tot = 0
        for entry in self.games:
            tot += entry
        return (tot / self.size())
    
class AdjMatrixGraph:
    def __init__ (self):
        self.n = 0
        self.array = []
        self.arraynames = []

    def display (self):
        for x in range (self.n):
            for y in range (self.n):
                if (self.array[x][y].size() == 0):
                    entry = "n"
                else:
                    entry = str(self.array[x][y].games[0])
                    for q in range(1, self.array[x][y].size()):
                        entry += ", " + str(self.array[x][y].games[q])
                print (entry, end="\t")
            print( )
        print( )

    def insert (self, x, y, w):
        self.array[x][y] = int(w)
        
    def update(self):
        if len(self.array) < self.n:
            x = self.n - len(self.array)
            for q in range(0, x):
                for row in self.array:
                    row.append(Games())
            for q in range(0,x):
                new = []
                for y in range(self.n):
                    new.append(Games())
                self.array.append(new)

    def read(self, file):
        reader = open(file, "r")
        for line in reader:
            q = str(line).split()
            while len(q) > 4:
                if not(q[1].isdigit()):
                    temp = q[1]
                    q.remove(temp)
                    q[0] = q[0] + " " + temp
                elif not(q[3].isdigit()):
                    temp = q[3]
                    q.remove(temp)
                    q[2] = q[2] + " " + temp
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
            self.array[x][y].add(int(q[1]) - int(q[3]))
            self.array[y][x].add(int(q[3]) - int(q[1]))
    def swap(self, a, b, c):
        temp = a[b]
        a[b] = a[c]
        a[c] = temp
    def rate(self, filename):
        performance = []
        for team in self.array:
            total = 0
            count = 0
            for scores in team:
                total += scores.avg() * scores.size()
                count += scores.size()
            performance.append(total / count)
        rating = copy.deepcopy(performance)
        for n in range(5000):
            schedule_factor = []
            for x in range(len(self.array)):
                temp = 0
                count = 0
                for y in range(len(self.array)):
                    if not(self.array[x][y].size() == 0):
                        temp += rating[y] * self.array[x][y].size()
                        count += self.array[x][y].size()
                schedule_factor.append(temp / count)
            for q in range(len(rating)):
                rating[q] = performance[q] + schedule_factor[q]
        f = open("output_" + filename, 'w')
        f.write("Rank Team                            W-L-T    Rating\n")
        for i in range(len(rating)):
            least = i
            for k in range(i + 1, len(rating)):
                if rating[k] > rating[least]:
                    least = k
            self.swap(rating, least, i)
            self.swap(self.arraynames, least, i)
            self.swap(self.array, least, i)
        for number in range(len(rating)):
            for go in range(int(3 - len(str(number + 1)))):
                f.write(" ")
            f.write(str(number+1) + "  " + str(self.arraynames[number]))
            for go in range(int((32 - len(self.arraynames[number])))):
                f.write(" ")
            wins = 0
            losses = 0
            ties = 0
            for thingy in self.array[number]:
                for score in thingy.games:
                    if score > 0:
                        wins += 1
                    elif score < 0:
                        losses += 1
                    else:
                        ties += 1
            out = str(format(rating[number], '.1f'))
            f.write(str(wins) + "-" + str(losses) + "-" + str(ties))
            for go in range(int(10 - len(out))):
                f.write(" ")
            f.write(out + "\n")
                    
            

def main():
    graph = AdjMatrixGraph()
    filename = input("Filename? ")
    graph.read(filename)
    graph.rate(filename)

main()











            
