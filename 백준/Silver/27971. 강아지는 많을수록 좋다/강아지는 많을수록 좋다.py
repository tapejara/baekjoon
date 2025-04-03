from collections import deque
import sys
input = sys.stdin.readline
n, m, a, b = map(int,input().split())
dog = [-1 for _ in range(n + 1)]
for _ in range(m):
    l, r = map(int,input().split())
    for i in range(l, r + 1):
        dog[i] = 0
q = deque([(0, 0)])
while q:
    c, count = q.popleft()
    if(c == n):
        break
    for i in [a, b]:
        if(c + i <= n and dog[c + i] == -1):
            q.append((c + i, count + 1))
            dog[c + i] = count + 1
print(dog[-1])