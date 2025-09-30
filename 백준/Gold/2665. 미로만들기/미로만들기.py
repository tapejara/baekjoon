from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
edge = [[] for _ in range(n)]
for i in range(n):
    temp = str(input().strip())
    for j in range(n):
        edge[i].append(int(temp[j]))
dist = [[1e99 for _ in range(n)] for _ in range(n)]
dist[0][0] = 0
q = deque([(0,0)])
while q:
    current_x, current_y = q.popleft()
    for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
        if(-1 < current_x + x < n and -1 < current_y + y < n and edge[current_y + y][current_x + x] == 1 and dist[current_y + y][current_x + x] > dist[current_y][current_x]):
            dist[current_y + y][current_x + x] = dist[current_y][current_x]
            q.appendleft((current_x + x, current_y + y))
        elif(-1 < current_x + x < n and -1 < current_y + y < n and edge[current_y + y][current_x + x] == 0 and dist[current_y + y][current_x + x] > dist[current_y][current_x] + 1):
            dist[current_y + y][current_x + x] = dist[current_y][current_x] + 1
            q.appendleft((current_x + x, current_y + y))

print(dist[-1][-1])