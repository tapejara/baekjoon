from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [[i for i in input().strip()] for _ in range(n)]
dist = [[1e99 for _ in range(m + 1)] for _ in range(n + 1)]
dist[0][0] = 0
q = deque([(0, 0)])
list2 = [(-1,-1), (0,-1), (0,0), (-1,0)]
list3 = [(-1,-1), (1,-1), (1,1), (-1,1)]
def function(x0,y0,x1,y1,x2,y2,z):
    if(list1[y2][x2] == "\\"):
        if(z % 2 == 0 and dist[y1][x1] > dist[y0][x0]):
            dist[y1][x1] = dist[y0][x0]
            q.appendleft((x1,y1))
        elif(z % 2 == 1 and dist[y1][x1] > dist[y0][x0] + 1):
            dist[y1][x1] = dist[y0][x0] + 1
            q.append((x1,y1))
    elif(list1[y2][x2] == "/"):
        if(z % 2 == 0 and dist[y1][x1] > dist[y0][x0] + 1):
            dist[y1][x1] = dist[y0][x0] + 1
            q.append((x1,y1))
        elif(z % 2 == 1 and dist[y1][x1] > dist[y0][x0]):
            dist[y1][x1] = dist[y0][x0]
            q.appendleft((x1,y1))
while q:
    current_x, current_y = q.popleft()
    for i in range(4):
        if(-1 < current_x + list3[i][0] < m + 1 and -1 < current_y + list3[i][1] < n + 1):
            function(current_x, current_y, current_x + list3[i][0],current_y + list3[i][1], current_x + list2[i][0], current_y + list2[i][1], i)
if(dist[-1][-1] == 1e99):
    print("NO SOLUTION")
else:
    print(dist[-1][-1])