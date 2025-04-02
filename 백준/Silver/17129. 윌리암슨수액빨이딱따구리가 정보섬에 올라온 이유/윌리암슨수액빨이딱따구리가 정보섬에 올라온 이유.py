from collections import deque
import sys
input = sys.stdin.readline
m, n = map(int,input().split())
space = [[int(c) for c in input().strip()] for _ in range(m)]
visted = [[0 for _ in range(n)] for _ in range(m)]
q = deque([])
for i in range(m):
    for j in range(n):
        if(space[i][j] == 2):
            visted[i][j] = 1
            q.append((j, i, 0))
while q:
    x, y, count = q.popleft()
    if(space[y][x] == 3 or space[y][x] == 4 or space[y][x] == 5):
        print("TAK")
        print(count)
        exit()
    shift = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for a,b in shift:
        if(-1 < x + a < n and -1 < y + b < m and space[y + b][x + a] != 1 and visted[y + b][x + a] == 0):
            q.append((x + a , y + b, count + 1))
            visted[y + b][x + a] = 1
print("NIE") 