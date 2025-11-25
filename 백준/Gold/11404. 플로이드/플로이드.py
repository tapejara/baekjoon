import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
dist = [[1e99 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    dist[a][b] = min(dist[a][b], c)
for i in range(n):
    dist[i][i] = 0
    for j in range(n):
        for k in range(n):
            if(dist[j][k] > dist[j][i] + dist[i][k]):
                dist[j][k] = dist[j][i] + dist[i][k]
for i in range(n):
    for j in range(n - 1):
        if(dist[i][j] == 1e99):
            print(0, end = " ")
        else:
            print(dist[i][j], end = " ")
    if(dist[i][n - 1] == 1e99):
        print(0)
    else:
        print(dist[i][n - 1])