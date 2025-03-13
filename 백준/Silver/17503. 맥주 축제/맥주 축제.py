import sys, heapq
input = sys.stdin.readline
n, m, k = map(int,input().split())
beer = list(tuple(map(int,input().split())) for _ in range(k))
beer.sort(key = lambda x: x[1])
hq = []
total = 0
level = -1
for i in range(len(beer)):
    heapq.heappush(hq, beer[i][0])
    total += beer[i][0]
    if(len(hq) == n and total < m):
        total -= heapq.heappop(hq)
    elif(len(hq) == n and total >= m):
        level = beer[i][1]
        break
print(level)