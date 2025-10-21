import heapq, sys
input = sys.stdin.readline
k, n, m = map(int,input().split())
list1 = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, t, h = map(int,input().split())
    list1[a].append((b, t, h))
    list1[b].append((a, t, h))
dist_list = [[1e99 for _ in range(k + 1)] for _ in range(n + 1)]
start, end = map(int,input().split())
for i in range(k + 1):
    dist_list[start][i] = 0
q = [(0, k, start)]
while q:
    dist, curent_k, current_p = heapq.heappop(q)
    if(dist_list[current_p][curent_k] < dist):
        continue
    for next_p, next_t, next_h in list1[current_p]:
        if(curent_k - next_h > 0 and dist_list[next_p][curent_k - next_h] > dist_list[current_p][curent_k] + next_t):
            dist_list[next_p][curent_k - next_h] = dist_list[current_p][curent_k] + next_t
            heapq.heappush(q, (dist_list[next_p][curent_k - next_h], curent_k - next_h, next_p))
if(min(dist_list[end]) == 1e99):
    print(-1)
else:
    print(min(dist_list[end]))