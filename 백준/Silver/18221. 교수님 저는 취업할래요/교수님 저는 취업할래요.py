n = int(input())
e = 0
point5 = []
point2 = []
listS = []
for i in range(n):
    list1 = list(map(int,input().split()))
    if(5 in list1):
        point5.append(list1.index(5))
        point5.append(i)
    if(2 in list1):
        point2.append(list1.index(2))
        point2.append(i)
    for j in range(n):
        if(list1[j] == 1):
            listS.append([j,i])
if((((point5[0] - point2[0]) ** 2) + ((point5[1] - point2[1]) ** 2)) ** 0.5) < 5 :
    print(0)
elif(len(listS) < 3):
    print(0)
else:
    for k in range(len(listS)):
        if(min(point5[0],point2[0]) <= listS[k][0] <= max(point5[0],point2[0]) and min(point5[1],point2[1]) <= listS[k][1] <= max(point5[1],point2[1])):
            e += 1
    if(e >= 3):
        print(1)
    else:
        print(0)