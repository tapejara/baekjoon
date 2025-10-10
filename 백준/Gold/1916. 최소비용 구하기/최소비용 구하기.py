import heapq, sys
input = sys.stdin.readline
n = int(input())
m = int(input())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, k = map(int,input().split())
    edge[i].append((j, k))
start, end = map(int,input().split())
dist = [1e99 for _ in range(n + 1)]
dist[start] = 0
q = [(0,start)]
while q:
    cost, point = heapq.heappop(q)
    if(dist[point] < cost):
        continue
    for x, y in edge[point]:
        if(dist[x] > dist[point] + y):
            dist[x] = dist[point] + y
            heapq.heappush(q,(dist[x], x))
print(dist[end])