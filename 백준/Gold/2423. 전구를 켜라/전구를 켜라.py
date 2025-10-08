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
while q:
    current_x, current_y = q.popleft()
    for i in range(4):
        if(-1 < current_x + list3[i][0] < m + 1 and -1 < current_y + list3[i][1] < n + 1):
            if(list1[current_y + list2[i][1]][current_x + list2[i][0]] ==  "\\"):
                if(i % 2 == 0 and dist[current_y + list3[i][1]][current_x + list3[i][0]] > dist[current_y][current_x]):
                    dist[current_y + list3[i][1]][current_x + list3[i][0]] = dist[current_y][current_x]
                    q.appendleft((current_x + list3[i][0], current_y + list3[i][1]))
                elif(i % 2 == 1 and dist[current_y + list3[i][1]][current_x + list3[i][0]] > dist[current_y][current_x] + 1):
                    dist[current_y + list3[i][1]][current_x + list3[i][0]] = dist[current_y][current_x] + 1
                    q.append((current_x + list3[i][0], current_y + list3[i][1]))
            elif(list1[current_y + list2[i][1]][current_x + list2[i][0]] ==  "/"):
                if(i % 2 == 1 and dist[current_y + list3[i][1]][current_x + list3[i][0]] > dist[current_y][current_x]):
                    dist[current_y + list3[i][1]][current_x + list3[i][0]] = dist[current_y][current_x]
                    q.appendleft((current_x + list3[i][0], current_y + list3[i][1]))
                elif(i % 2 == 0 and dist[current_y + list3[i][1]][current_x + list3[i][0]] > dist[current_y][current_x] + 1):
                    dist[current_y + list3[i][1]][current_x + list3[i][0]] = dist[current_y][current_x] + 1
                    q.append((current_x + list3[i][0], current_y + list3[i][1]))
if(dist[-1][-1] == 1e99):
    print("NO SOLUTION")
else:
    print(dist[-1][-1])