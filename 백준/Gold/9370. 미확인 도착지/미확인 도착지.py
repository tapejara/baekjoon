import heapq, sys
input = sys.stdin.readline
z = int(input())
for _ in range(z):
    n, m, t = map(int,input().split())
    s, g, h = map(int,input().split())
    list1 = [[] for _ in range(n + 1)]
    dist_gh = 0
    for i in range(m):
        a, b, d = map(int,input().split()) 
        if((a == g and b == h) or (a == h and b == g)):
            dist_gh = d
        list1[a].append((b, d))
        list1[b].append((a, d))
    dist_list1 = [1e99 for _ in range(n + 1)]
    dist_list2 = [1e99 for _ in range(n + 1)]
    dist_list3 = [1e99 for _ in range(n + 1)]
    dist_list1[s] = 0
    q1 = [(0, s)]
    while q1:
        dist, point = heapq.heappop(q1)
        if(dist > dist_list1[point]):
            continue
        for next_point, next_dist in list1[point]:
            if(dist_list1[next_point] > dist_list1[point] + next_dist):
                dist_list1[next_point] = dist_list1[point] + next_dist
                heapq.heappush(q1, (dist_list1[next_point], next_point))
    dist_list2[g] = dist_list1[h] + dist_gh
    q2 = [(dist_list2[g], g)]
    while q2:
        dist, point = heapq.heappop(q2)
        if(dist > dist_list2[point]):
            continue
        for next_point, next_dist in list1[point]:
            if(dist_list2[next_point] > dist_list2[point] + next_dist):
                dist_list2[next_point] = dist_list2[point] + next_dist
                heapq.heappush(q2, (dist_list2[next_point], next_point))
    dist_list3[h] = dist_list1[g] + dist_gh
    q3 = [(dist_list3[h], h)]
    while q3:
        dist, point = heapq.heappop(q3)
        if(dist > dist_list3[point]):
            continue
        for next_point, next_dist in list1[point]:
            if(dist_list3[next_point] > dist_list3[point] + next_dist):
                dist_list3[next_point] = dist_list3[point] + next_dist
                heapq.heappush(q3, (dist_list3[next_point], next_point))
    list2 = [[] for _ in range(n + 1)]
    list3 = []
    for _ in range(t):
        x = int(input())
        list3.append(x)
        list2[x].append(dist_list2[x])
        list2[x].append(dist_list3[x])
    list3.sort()
    answer = []
    for i in range(t):
        if(min(list2[list3[i]]) == dist_list1[list3[i]] and min(list2[list3[i]]) != 1e99):
            answer.append(list3[i])
    if(answer):
        for i in range(len(answer) - 1):
            print(answer[i], end= " ")
        print(answer[-1])