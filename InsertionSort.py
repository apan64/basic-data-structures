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


  
                
