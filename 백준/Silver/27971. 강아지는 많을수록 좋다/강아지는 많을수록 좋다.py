from collections import deque
import sys
input = sys.stdin.readline
n, m, a, b = map(int,input().split())
dog = [0 for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int,input().split())
    for i in range(l, r + 1):
        dog[i] = 1
q = deque([(0, 0)])
while q:
    c, count = q.popleft()
    if(c == n):
        print(count)
        exit()
    if(c + a <= n and dog[c + a] != 1):
        q.append((c + a, count + 1))
        dog[c + a] = 1
    if(c + b <= n and dog[c + b] != 1):
        q.append((c + b, count + 1))
        dog[c + b] = 1
print(-1)