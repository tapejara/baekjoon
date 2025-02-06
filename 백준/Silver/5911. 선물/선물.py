import sys
input = sys.stdin.readline
n, b = map(int,input().split())
list1 = []
list2 = []
list3 = []
for _ in range(n):
    p, s = map(int,input().split())
    list1.append([p + s ,(p,s)])
    list2.append([(p, s), p // 2 + s])
list1.sort(key = lambda x:x[0])
for i in range(n):
    if(list2[i][1] > b):
        list3.append(0)
        continue
    total_prince = list2[i][1]
    total_friends = 1
    flag = True
    for j in range(n):
        if(list2[i][0] == list1[j][1] and flag == True):
            flag = False
            continue
        else:
            if(total_prince + list1[j][0] > b):
                break
            total_prince += list1[j][0]
            total_friends += 1
    list3.append(total_friends)
print(max(list3))