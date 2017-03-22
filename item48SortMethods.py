def bubbleSort(x):
    for passnum in range(len(x)-1,0,-1):
        for i in range(passnum):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

x = [67,45,2,13,1,998]
bubbleSort(x)
print(x)

def selectionSort(x):
    for fillslot in range(len(x)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if x[location]>x[positionOfMax]:
                positionOfMax = location

        temp = x[fillslot]
        x[fillslot] = x[positionOfMax]
        x[positionOfMax] = temp

x = [89,23,33,45,10,12,45,45,45]
selectionSort(x)
print(x)
