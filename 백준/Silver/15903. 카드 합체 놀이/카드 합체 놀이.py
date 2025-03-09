import sys, heapq
input = sys.stdin.readline
n, m  = map(int,input().split())
hq = list(map(int,input().split()))
heapq.heapify(hq)
for i in range(m):
    x = heapq.heappop(hq)
    y = heapq.heappop(hq)
    heapq.heappush(hq, x + y)
    heapq.heappush(hq, x + y)
print(sum(hq))