import sys, heapq
input = sys.stdin.readline
n, m, k = map(int,input().split())
beer = []
vi = []
level = 0
for _ in range(k):
    v, c = map(int,input().split())
    heapq.heappush(beer,(c, v))
for _ in range(n):
    pop1 =  heapq.heappop(beer)
    heapq.heappush(vi,pop1[1])
    m -= pop1[1]
    level = pop1[0]
if(m > 0):
    while m > 0 and beer:
        pop2 = heapq.heappop(vi)
        pop3 = heapq.heappop(beer)
        heapq.heappush(vi,pop3[1])
        m += pop2
        m -= pop3[1]
        level = pop3[0]
    if(m > 0):
        print(-1)
    else:
        print(level)
else:
    print(level)