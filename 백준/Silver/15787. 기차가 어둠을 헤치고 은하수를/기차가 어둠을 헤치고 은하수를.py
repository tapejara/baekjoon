n, m = map(int,input().split()) 
list1 = [[0 for _ in range(20)] for _ in range(n)]
list2 = []
for _ in range(m):
    list3 = list(map(int,input().split()))
    if(list3[0] == 1):
        list1[list3[1] - 1][list3[2] - 1] = 1
    elif(list3[0] == 2):
        list1[list3[1] - 1][list3[2] - 1] = 0
    elif(list3[0] == 3):
        list1[list3[1] - 1] = [0] + list1[list3[1] - 1][:19].copy()
    elif(list3[0] == 4):
        list1[list3[1] - 1] = list1[list3[1] - 1][1:] + [0]
for i in range(n):
    if(list1[i] not in list2):
        list2.append(list1[i])
print(len(list2))