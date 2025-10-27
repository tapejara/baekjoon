import heapq, sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
list1 = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j, l = map(int,input().split())
    list1[i].append((j, l))
    list1[j].append((i, l))
time_list = [[1e99 for _ in range(k + 1)] for _ in range(n + 1)]
time_list[1][k] = 0
q = [(0, 1, k)]
while q:
    time, point, cost = heapq.heappop(q)
    if(time > time_list[point][cost]):
        continue
    for next_p, next_t in list1[point]:
        if(cost > 0):
            if(time_list[next_p][cost] > time_list[point][cost] + next_t):
                time_list[next_p][cost] = time_list[point][cost] + next_t
                heapq.heappush(q, (time_list[next_p][cost], next_p, cost))
            if(time_list[next_p][cost - 1] > time_list[point][cost]):
                time_list[next_p][cost - 1] = time_list[point][cost]
                heapq.heappush(q, (time_list[next_p][cost - 1], next_p, cost - 1))
        else:
            if(time_list[next_p][cost] > time_list[point][cost] + next_t):
                time_list[next_p][cost] = time_list[point][cost] + next_t
                heapq.heappush(q, (time_list[next_p][cost], next_p, cost))
print(min(time_list[n]))