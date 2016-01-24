import sys

def genHibbard(z):
    file = open("Hibbard.txt", "w")
    x = 1
    while ((2**x)-1) < z:
        file.write(str((2**x)-1) + "\n")
        x += 1
    file.close()
    
def genPratt(z):
    file = open("Pratt.txt", "w")
    x = 0
    y = 0
    array = []
    array.append(1)
    file.write(str(1) + "\n")
    a = 1
    current = 0
    while current < z:
        if ((array[x]*2) < (array[y]*3)):
            array.append(array[x] * 2)
            x += 1
        elif ((array[x]*2) > (array[y]*3)):
            array.append(array[y] * 3)
            y += 1
        else:
            array.append(array[x] * 2)
            x += 1
            y += 1
        current = array[a]
        if current < z:
            file.write(str(array[a]) +"\n")
        a += 1
    file.close()
    
def genSedgeA(z):
    file = open("SedgewickA.txt", "w")
    file.write(str(1) + "\n")
    x = 1
    current = 0
    while current < z:
        current = (4**x)+3*(2**(x-1))+1
        if current < z:
            file.write(str(current) + "\n")
        x += 1
    file.close()
    
def genSedgeB(z):
    file = open("SedgewickB.txt", "w")
    x = 1
    current = 0
    current2 = 0
    while current2 < z:
        current = 9*((4**(x-1))-(2**(x-1)))+1
        current2 = (4**(x+1))-6*(2**x)+1
        if current < z:
            file.write(str(current) + "\n")
        if current2 < z:
            file.write(str(current2) + "\n")
        x += 1
    file.close()

num = int(input("Largest gap? "))

genHibbard(num)
genPratt(num)
genSedgeA(num)
genSedgeB(num)
