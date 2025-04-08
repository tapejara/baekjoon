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
    goal = []
    for i in range(a, b + 1):
        if(i in prime):
            goal.append(i)
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
        if(num > b):
            if(visited[num // 2] == 0):
                q.append((num // 2, count + 1))
                visited[num // 2] = 1
            if(visited[num // 3] == 0):
                q.append((num // 3, count + 1))
                visited[num // 3] = 1
            if(visited[num - 1] == 0 and 0 <= num - 1):
                q.append((num - 1, count + 1))
                visited[num - 1] = 1
        elif(a <= num <= b):
            if(visited[num // 2] == 0):
                q.append((num // 2, count + 1))
                visited[num // 2] = 1
            if(visited[num // 3] == 0):
                q.append((num // 3, count + 1))
                visited[num // 3] = 1
            if(visited[num - 1] == 0 and 0 <= num - 1):
                q.append((num - 1, count + 1))
                visited[num - 1] = 1
            if(visited[num + 1] == 0 and num + 1 < len(visited)):
                q.append((num + 1, count + 1))
                visited[num + 1]
        elif(num < a):
            if(visited[num + 1] == 0 and num + 1 < len(visited)):
                q.append((num + 1, count + 1))
                visited[num + 1]