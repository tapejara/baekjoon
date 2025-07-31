n, m = map(int,input().split())
list1 = [[0,0] for _ in range(1000361)]
lista = list(set(map(int,input().split())))
listb = list(set(map(int,input().split())))
lista.sort()
listb.sort()
for i in range(len(lista)):
    list1[lista[i]][0] = 1
for i in range(len(listb)):
    list1[listb[i]][1] = 1
for i in range(len(list1)):
    if(list1[i][0] == 1 or list1[i][1] == 1):
        if(list1[i][0] == 1):
            for j in range(i + 1, i + 100):
                list1[j][0] = 0
        if(list1[i][1] == 1):
            for j in range(i + 1, i + 360):
                list1[j][1] = 0
nova = 0
origin = 0
for i in range(len(list1)):
    if(list1[i][0] == 1):
        nova += 1
    if(list1[i][1] == 1):
        origin += 1
print(nova, origin)