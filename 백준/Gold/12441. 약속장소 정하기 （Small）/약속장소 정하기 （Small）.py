import heapq, sys
input = sys.stdin.readline
t = int(input())
for i in range(1, t + 1):
    n, p, m = map(int,input().split())
    fre = []
    for _ in range(p):
        x, v = map(int,input().split())
        fre.append((x, v))
    city = [[] for _ in range(n + 1)]
    dist_list = [[1e99 for _ in range(p)] for _ in range(n + 1)]
    for j in range(m):
        list1 = list(map(int,input().split()))
        for k in range(2, len(list1) - 1):
            city[list1[k]].append((list1[k + 1], list1[0]))
            city[list1[k + 1]].append((list1[k], list1[0]))
    for j in range(p):
        start = fre[j][0]
        time = fre[j][1]
        dist_list[start][j] = 0
        q = [(0,start)] 
        while q:
            dist, current = heapq.heappop(q)
            if(dist > dist_list[current][j]):
                continue
            for a,b in city[current]:
                if(dist_list[a][j] > dist_list[current][j] + b * time):
                    dist_list[a][j] = dist_list[current][j] + b * time
                    heapq.heappush(q, (dist_list[a][j], a))
    answer = []
    for j in range(1, n + 1):
        answer.append(max(dist_list[j]))
    if(min(answer) == 1e99):
        print(f"Case #{i}: {-1}")
    else:
        print(f"Case #{i}: {min(answer)}")