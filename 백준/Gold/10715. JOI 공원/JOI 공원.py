import heapq, sys
input = sys.stdin.readline
n, m, c = map(int,input().split())
list1 = [[] for _ in range(n + 1)]
set1 = set()
total = 0
for i in range(m):
    a, b, d = map(int,input().split())
    total += d
    list1[a].append((b, d))
    list1[b].append((a, d))
dist_list = [1e99 for _ in range(n + 1)]
dist_list[1] = 0
q1 = [(0, 1)]
cost = total
answer = 1e99
while q1:
    dist, point = heapq.heappop(q1)
    if(dist > dist_list[point]):
        continue
    if(point not in set1):
        set1.add(point)
        temp = 0
        for next_p, next_d in list1[point]:
            if(dist_list[next_p] > dist_list[point] + next_d):
                dist_list[next_p] = dist_list[point] + next_d
                heapq.heappush(q1, (dist_list[next_p], next_p))
            if(next_p in set1):
                temp += next_d
        cost -= temp
        answer = min(answer, cost + c * dist_list[point])
    else:
        continue
print(answer)