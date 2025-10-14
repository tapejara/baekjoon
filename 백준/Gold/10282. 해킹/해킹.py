import heapq, sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, d, c = map(int,input().split())
    list1 = [[] for _ in range(n + 1)]
    dist_list = [1e99 for _ in range(n + 1)]
    dist_list[c] = 0
    for _ in range(d):
        a, b, s = map(int,input().split())
        list1[b].append((a, s))
    q = [(0,c)]
    while q:
        dist, current = heapq.heappop(q)
        if(dist > dist_list[current]):
            continue
        for next, time in list1[current]:
            if(dist_list[next] > dist_list[current] + time):
                dist_list[next] = dist_list[current] + time
                heapq.heappush(q, (dist_list[next], next))
    answer = []
    for i in range(n + 1):
        if(dist_list[i] != 1e99):
            answer.append(dist_list[i])
    print(len(answer), max(answer))