from collections import deque
n, m = map(int,input().split())
material = [[int(c) for c in input()] for _ in range(n)]
start = []
for i in range(m):
    if(material[0][i] == 0):
        start.append((i,0))
        material[0][i] = 1
q = deque(start)
while q:
    x, y = q.popleft()
    if(y == n - 1):
        print("YES")
        exit()
    for a,b in [(0,1), (0,-1), (1,0), (-1,0)]:
        if(-1 < x + a < m and -1 < y + b < n and material[y + b][x + a] == 0):
            q.append((x + a, y + b))
            material[y + b][x + a] = 1
print("NO")