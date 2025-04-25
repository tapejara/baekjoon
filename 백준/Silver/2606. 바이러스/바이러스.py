from collections import deque
n = int(input())
t = int(input())
link = [tuple(map(int,input().split())) for _ in range(t)]
visited = [0 for _ in range(n + 1)]
start = 1
q = deque([start])
while q:
    point = q.popleft()
    visited[point] = 1
    for x, y in link:
        if(point == x and visited[y] == 0):
            q.append(y)
        elif(point == y and visited[x] == 0):
            q.append(x)
print(visited.count(1) - 1)