import itertools
n = int(input())
list1 = [tuple(map(int,input().split())) for _ in range(n)]
list2 = list(itertools.combinations(list1, 3))
list3 = []
for i in range(len(list2)):
    a = list2[i][0][0] * list2[i][1][1] + list2[i][1][0] * list2[i][2][1] + list2[i][2][0] * list2[i][0][1]
    b = list2[i][1][0] * list2[i][0][1] + list2[i][2][0] * list2[i][1][1] + list2[i][0][0] * list2[i][2][1]
    list3.append(abs(a - b) / 2)
print(max(list3))