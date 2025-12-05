import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dist = [[1e99 for _ in range(n)] for _ in range(n)]
count = 0
for i in range(n - 1):
    temp = list(map(int,input().split()))
    for j in range(len(temp)):
        dist[i][j + i + 1] = temp[j] 
        dist[j + i + 1][i] = temp[j]
        count += 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            if(dist[j][k] != 1e99 and dist[j][k] >= dist[j][i] + dist[i][k] and count > m):
                dist[j][k] = 1e99
                dist[k][j] = 1e99
                count -= 1
answer = []
check = []
for i in range(n):
    for j in range(n):
        if(dist[i][j] != 1e99 and set([i + 1, j + 1]) not in check):
            answer.append((i + 1, j + 1, dist[i][j]))
            check.append(set([i + 1, j + 1]))
if(len(answer) == m):
    print(1)
    for i in range(m):
        for j in range(3):
            print(answer[i][j], end = " ")
        print()
else:
    print(0)