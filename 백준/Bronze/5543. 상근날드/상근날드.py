listb = []
for i in range(3):
    a = int(input())
    listb.append(a)
listd = []
for _ in range(2):
    b = int(input())
    listd.append(b)
combi = []
for burger in listb:
    for drink in listd:
        combi.append(burger + drink - 50)
print(min(combi))