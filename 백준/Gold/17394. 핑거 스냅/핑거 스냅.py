from collections import deque
import sys
input = sys.stdin.readline
prime = set(i for i in range(2, 100001))
for i in range(2,100001):
    if(i in prime):
        prime -= set(j for j in range(i * 2, 100001, i))
t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    goal = set()
    for i in range(a, b + 1):
        if(i in prime):
            goal.add(i)
    if(len(goal) == 0):
        print(-1)
        continue
    visited = [0 for _ in range(1000001)]
    q = deque([(n,0)])
    while q:
        num, count = q.popleft()
        if(num in goal):
            print(count)
            break
        for i in [2, 3]:
            if(0 <= num // i <= 1000000 and visited[num // i] == 0):
                q.append((num // i, count + 1))
                visited[num // i] = 1
        for i in [1, -1]:
            if(0 <= num + i <= 1000000 and visited[num + i] == 0):
                q.append((num + i, count + 1))
                visited[num + i] = 1