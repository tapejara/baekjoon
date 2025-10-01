from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
y1, x1, y2, x2 = map(int,input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
edge = [[i for i in str(input().strip())] for _ in range(n)]
dist = [[1e99 for _ in range(m)] for _ in range(n)]
edge[y1][x1] = "0"
edge[y2][x2] = "1"
dist[y1][x1] = 1
q = deque([(x1,y1)])
while q:
    current_x, current_y = q.popleft()
    for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
        if(-1 < current_x + x < m and -1 < current_y + y < n and edge[current_y][current_x] == "0" and dist[current_y + y][current_x + x] > dist[current_y][current_x]):
            dist[current_y + y][current_x + x] = dist[current_y][current_x]
            q.appendleft((current_x + x, current_y + y))
        elif(-1 < current_x + x < m and -1 < current_y + y < n and edge[current_y][current_x] == "1" and dist[current_y + y][current_x + x] > dist[current_y][current_x] + 1):
            dist[current_y + y][current_x + x] = dist[current_y][current_x] + 1
            q.append((current_x + x, current_y + y))
print(dist[y2][x2])