import heapq
from collections import deque
m, n = map(int,input().split())
edge = [[] for _ in range(m)]
for _ in range(n):
    i, j, dist = map(int,input().split())
    edge[i].append((j,dist))
dist_list = [[1e99,1e99] for _ in range(m)]
dist_list[0] = [0, 0]
q = [(0, 0)]
while q:
    dist1, current = heapq.heappop(q)
    for next, next_dist in edge[current]:
        if(dist_list[next][0] >= dist_list[current][0] + 1 and dist_list[next][1] > dist_list[current][1] + next_dist):
            dist_list[next][0] = dist_list[current][0] + 1
            dist_list[next][1] = dist_list[current][1] + next_dist
            heapq.heappush(q,(dist_list[next][0], next))
print(dist_list[1][1])