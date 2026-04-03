import heapq, sys
input = sys.stdin.readline
n, m = map(int,input().split())
edge = [[] for _ in range(n + 1)]
start = int(input())
for _ in range(m):
    i, j, k = map(int,input().split())
    edge[i].append((j, k))
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
for i in range(1, n + 1):
    if(dist[i] >= 1e99):
        print("INF")
    else:
        print(dist[i])