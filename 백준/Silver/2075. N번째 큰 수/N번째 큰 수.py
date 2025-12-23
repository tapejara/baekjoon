import sys, heapq
input = sys.stdin.readline
n = int(input())
t = []
for num in list(map(int,input().split())):
    heapq.heappush(t, num)
a = heapq.heappop(t)
for i in range(n - 1):
    temp = list(map(int,input().split()))
    for j in range(n):
        if(a < temp[j]):
            heapq.heappush(t, temp[j])
            a = heapq.heappop(t)
print(a)