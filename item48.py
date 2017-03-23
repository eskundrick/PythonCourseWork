
def sort_bubble(x):
    for reorder in range(len(x)-1,0,-1):
        for i in range(reorder):
            if x[i]>x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp

lista = [67,45,2,13,1,998]
listb = [89,23,33,45,10,12,45,45,45]

sort_bubble(lista)
print(lista)

sort_bubble(listb)
print(listb)



