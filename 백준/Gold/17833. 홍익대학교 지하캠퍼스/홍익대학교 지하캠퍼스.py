import heapq, sys
input = sys.stdin.readline
n = int(input())
r, d = map(int,input().split())
m = int(input())
list1 = [[] for _ in range(n + 1)]
for _ in range(m):
    h, t, e1, e2 = map(int,input().split())
    list1[e1].append((e2, h, t))
    list1[e2].append((e1, h, t))
dist_list = [1e99 for _ in range(n + 1)]
dist_list[r] = 0
q = [(0, r)]
while q:
    dist, depth = heapq.heappop(q)
    if(dist > dist_list[depth]):
        continue
    for i in range(depth + 1):
        for j in range(len(list1[i])):
            if(depth + (list1[i][j][1] - i) <= n and dist_list[depth + (list1[i][j][0] - i)] > dist + list1[i][j][2]):
                dist_list[depth + (list1[i][j][0] - i)] = dist + list1[i][j][2]
                heapq.heappush(q, (dist_list[depth + (list1[i][j][0] - i)], depth + (list1[i][j][0] - i)))
if(dist_list[d] == 1e99):
    print(-1)
else:
    print(dist_list[d])