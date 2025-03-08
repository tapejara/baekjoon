import sys, heapq
input = sys.stdin.readline
n, m, k = map(int,input().split())
duty = []
satisfaction = []
date = 0
for _ in range(n):
    heapq.heappush(duty, -int(input()))
while duty:
    a = -heapq.heappop(duty)
    if(satisfaction):
        satisfaction.append(satisfaction[-1] // 2 + a)
    else:
        satisfaction.append(a)
    if(a - m > k):
        heapq.heappush(duty, -(a - m))
    date += 1
print(date)
for element in satisfaction:
    print(element)