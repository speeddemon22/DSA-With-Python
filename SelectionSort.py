def SelectionSort(l):
    for start in range(len(l)):
        minpos = start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                temp = l[minpos]
                l[minpos] = l[i]
                l[i] = temp
    return(l)
li =[1,68,4,10]
t = SelectionSort(li)
print(t)