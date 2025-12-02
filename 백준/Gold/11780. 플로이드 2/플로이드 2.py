import sys
input = sys.stdin.readline
def function(a, b):
    if(node[a][b] == -1):
        return [0]
    path = [a]
    while a != b:
        a = node[a][b]
        path.append(a)
    return path
n = int(input())
m = int(input())
dist = [[1e99] * (n + 1) for _ in range(n + 1)]
node = [[-1] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    i, j, c = map(int,input().split())
    dist[i][j] = min(dist[i][j], c)
    node[i][j] = j
for i in range(1, n + 1):
    dist[i][i] = 0
    node[i][i] = -1
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if(dist[j][k] > dist[j][i] + dist[i][k]):
                dist[j][k] = dist[j][i] + dist[i][k]
                node[j][k] = node[j][i]
for i in range(1,n + 1):
    for j in range(1, n + 1):
        print(dist[i][j] if dist[i][j] != 1e99 else 0, end = " ")
    print()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        list1 = function(i, j)
        if(len(list1) != 1):
            print(len(list1), end = " ")
        for k in range(len(list1)):
            print(list1[k], end = " ")
        print()