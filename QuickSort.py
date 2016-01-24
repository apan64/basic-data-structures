import sys
import time

def quickSort(lyst):
    k = 2500
    def recurse(left, right):
        if left < right:
            pivotPosition = partition(lyst, left, right)
            if ((right - left) < k):
                IS(lyst, right - left)
            else:
                recurse(left, pivotPosition - 1);
                recurse(pivotPosition + 1, right)

    def partition(lyst, left, right):
        # Find the pivot and exchange it with the last item
        middle = (left + right) // 2
        pivot = lyst[middle]
        lyst[middle] = lyst[right]
        lyst[right] = pivot
        # Set boundary point to first position
        boundary = left
        # Move items less than pivot to the left
        for index in range(left, right):
            if lyst[index] < pivot:
                lyst[index],lyst[boundary] = lyst[boundary],lyst[index]
                boundary += 1
        # Exchange the pivot item and the boundary item
        lyst[right],lyst[boundary] = lyst[boundary],lyst[right]
        return boundary   
   
    recurse(0, len(lyst)-1)
    
def IS(a,length):
    minindex = 0
    for i in range(1,length,1):
        if (a[i] < a[minindex]): minindex = i
    a[0],a[minindex] = a[minindex],a[0]
    
    for i in range(2,length,1):
        j = i
        value = a[j]
        jm1 = j-1
        while (value < a[jm1]):
            a[j] = a[jm1]
            j = jm1
            jm1 = j-1
        a[j] = value
    
def main():

    filename = "file1"
    length = int(input("How many lines?"))
    a = []
    file = open(filename,"r")
    for i in range(0,length,1):
        a.append(int(file.readline()))

    t1 = time.process_time()
    quickSort(a)
    t2 = time.process_time()

    print (t2-t1)
#    print(a)

main()    
            
                
