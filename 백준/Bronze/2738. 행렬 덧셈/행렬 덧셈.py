b,a = map(int,input().split())
list1 = []
list2 = []
for _ in range(b):
    c = list(map(int,input().split()))
    list1.append(c)
for _ in range(b):
    c = list(map(int,input().split()))
    list2.append(c)
for i in range(b):
    for j in range(a):
        if(j == a-1):
            print(list1[i][j] + list2[i][j], end="\n")
        else:
            print(list1[i][j] + list2[i][j], end=" ")