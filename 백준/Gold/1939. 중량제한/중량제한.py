import heapq, sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [[] for _ in range(n + 1)]
weight_list = [0 for _ in range(n + 1)]
for _ in range(m):
    i, j, k = map(int,input().split())
    list1[i].append((j, k))
    list1[j].append((i, k))
start, end = map(int,input().split())
weight_list[start] = 1e99
q = [(-1e99, start)]
while q:
    w, p = heapq.heappop(q)
    w *= -1
    if(w < weight_list[p]):
        continue
    for next_p, next_w in list1[p]:
        if(w > next_w):
            if(next_w > weight_list[next_p]):
                weight_list[next_p] = next_w
                heapq.heappush(q, (-1 * next_w, next_p))
        else:
            if(w > weight_list[next_p]):
                weight_list[next_p] = w
                heapq.heappush(q, ( -1 * w, next_p))
print(weight_list[end])