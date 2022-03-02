def bubbleSort(alist):
    troca = True
    for passnum in range(len(alist)-1,0,-1):
        if not troca:
            break
        for i in range(passnum):
            troca = False
            if alist[i]>alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                troca = True

alist = [1,2,3,4,5,6]
bubbleSort(alist)
print(alis