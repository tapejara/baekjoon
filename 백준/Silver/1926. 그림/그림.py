from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
picture = [list(map(int,input().split())) for _ in range(n)]
visted = [[0 for _ in range(m)] for _ in range(n)]
extent = []
count = 0
for i in range(n):
    for j in range(m):
        w = 0
        if(picture[i][j] == 1 and visted[i][j] == 0):
            count += 1
            visted[i][j] = 1
            q = deque([(i, j)])
            shift = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                point1, point2 = q.popleft()
                w += 1
                for a,b in shift:
                    if(-1 < point1 + a < n and -1 < point2 + b < m):
                        if(visted[point1 + a][point2 + b] == 0 and picture[point1 + a][point2 + b] == 1):
                            visted[point1 + a][point2 + b] = 1
                            q.append((point1 + a, point2 + b))
        extent.append(w)
print(count)
print(max(extent))
