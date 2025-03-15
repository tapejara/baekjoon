import sys, heapq
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
hq = []
time = n * 24
total_score = sum(list1)
for i in range(m):
    heapq.heappush(hq, (-list2[i],list1[i]))
while time > 0 and hq:
    a = heapq.heappop(hq)
    current_score = a[1]
    bonus = 0
    while time > 0 and 100 - current_score >= -a[0]:
        time -= 1
        current_score -= a[0]
        bonus -= a[0]
    total_score += bonus
    if(100 - current_score > 0):
        heapq.heappush(hq, (current_score - 100, current_score))
print(total_score)
