import sys
import heapq
input = sys.stdin.readline
n, k = map(int,input().split())
team = [[] for _ in range(11)]
for _ in range(n):
    p, w =  map(int,input().split())
    heapq.heappush(team[p -1], -1 * w)
answer = []
for _ in range(k):
    total = 0
    for i in range(11):
        if(team[i]):
            mar_member = heapq.heappop(team[i])
            if(mar_member < 0):
                heapq.heappush(team[i], mar_member + 1)
            else:
                heapq.heappop(team[i], mar_member)
            nov_member = heapq.heappop(team[i])
            total += nov_member
            heapq.heappush(team[i], nov_member)
    answer.append(total)
print( -1 * answer[k - 1])