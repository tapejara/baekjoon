from collections import deque
n, m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]
answer = []
start = deque([])
for i in range(m):
    start.append((i, 0, space[0][i], 0))
while start:
    x, y, z, w = start.popleft()
    if(y == n - 1):
        answer.append(z)
    for a, b, c in [(0, 1, 1), (1, 1, 2), (-1, 1, 3)]:
        if(-1 < x + a < m and -1 < y + b < n and w != c):
            start.append((x + a, y + b, z + space[y + b][x + a], c))
print(min(answer))