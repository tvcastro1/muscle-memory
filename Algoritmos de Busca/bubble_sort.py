alist = [54,26,93,17,77,31,44,55,20]

x = 0
temp = 0
trocou = False

while x < len(alist) - 1:
    if alist[x] > alist[x + 1]:
        temp = alist[x]
        alist[x] = alist[x +1]
        alist[x + 1] = temp
        trocou = True
    x += 1
    print(alist)


