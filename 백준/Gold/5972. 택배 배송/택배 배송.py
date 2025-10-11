import heapq, sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, k = map(int,input().split())
    list1[i].append((j, k))
    list1[j].append((i, k))
dist = [1e99 for _ in range(n + 1)]
dist[1] = 0
q = [(0,1)]
while q:
    d, p = heapq.heappop(q)
    if(dist[p] < d):
        continue
    for x, y in list1[p]:
        if(dist[x] > dist[p] + y):
            dist[x] = dist[p] + y
            heapq.heappush(q, (dist[x], x))
print(dist[-1])