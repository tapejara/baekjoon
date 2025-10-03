from collections import deque
import sys
input = sys.stdin.readline
h, w = map(int,input().split())
oc = [[i for i in input().strip()] for _ in range(h)]
x1 = 0; y1 = 0; x2 = 0; y2 = 0
for i in range(h):
    for j in range(w):
        if(oc[i][j] == "K"):
            x1 = j; y1 = i
        elif(oc[i][j] == "*"):
            x2 = j; y2 = i
dist = [[1e99 for _ in range(w)] for _ in range(h)]
dist[y1][x1] = 0
q = deque([(x1, y1)])
while q:
    current_x, current_y = q.popleft()
    for x, y in [(1,1), (1,0), (1,-1)]:
        if(-1 < current_x + x < w and -1 < current_y + y < h and oc[current_y+ y][current_x + x] != "#" and dist[current_y + y][current_x + x] > dist[current_y][current_x]):
            dist[current_y + y][current_x + x] = dist[current_y][current_x]
            q.appendleft((current_x + x, current_y + y))
    for x, y in [(0,1), (0,-1), (-1,-1), (-1,0), (-1,1)]:
        if(-1 < current_x + x < w and -1 < current_y + y < h and oc[current_y+ y][current_x + x] != "#" and dist[current_y + y][current_x + x] > dist[current_y][current_x] + 1):
            dist[current_y + y][current_x + x] = dist[current_y][current_x] + 1
            q.append((current_x + x, current_y + y))
if(dist[y2][x2] == 1e99):
    print(-1)
else:
    print(dist[y2][x2])