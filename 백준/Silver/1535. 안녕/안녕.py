import itertools
n = int(input())
list1 = [[] for _ in range(n)]
input_1 = list(map(int,input().split()))
for i in range(n):
    list1[i].append(input_1[i])
input_2 = list(map(int,input().split()))
for i in range(n):
    list1[i].append(input_2[i])
list2 = []
for i in range(1,n + 1):
    temp = list(itertools.combinations(list1, i))
    for element in temp:
        list2.append(element)
list3 = []
for i in range(len(list2)):
    a = 0
    b = 0
    for j in range(len(list2[i])):
        a += list2[i][j][0]
        b += list2[i][j][1]
    if(a < 100):
        list3.append(b)
if(list3):
    print(max(list3))
else:
    print(0)