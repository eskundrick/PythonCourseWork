def sort_bubble(x):
    for reorder in range(len(x)-1,0,-1):
        for i in range(reorder):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

x = [67,45,2,13,1,998]
sort_bubble(x)
print(x)

def sort_bubble(x):
    for reorder in range(len(x)-1,0,-1):
        for i in range(reorder):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

x = [89,23,33,45,10,12,45,45,45]
sort_bubble(x)
print(x)
