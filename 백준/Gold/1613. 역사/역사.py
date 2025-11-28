import sys
input = sys.stdin.readline
n, k = map(int,input().split())
list1 = [[1e99 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    list1[a][b] = min(list1[a][b], 1)
for i in range(n):
    list1[i][i] = 0
    for j in range(n):
        for k in range(n):
            if(list1[j][k] > list1[j][i] + list1[i][k]):
                list1[j][k] = list1[j][i] + list1[i][k]
s = int(input())
for i in range(s):
    c, d = map(int,input().split())
    c -= 1
    d -= 1
    if(list1[c][d] < list1[d][c]):
        print(-1)
    elif(list1[c][d] > list1[d][c]):
        print(1)
    elif(list1[c][d] == list1[d][c]):
        print(0)