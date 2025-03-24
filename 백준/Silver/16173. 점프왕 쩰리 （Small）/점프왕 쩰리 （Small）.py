from collections import deque
n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]
start = [0, 0]
q = deque([start])
while q:
    a = q.popleft()
    b = m[a[1]][a[0]]
    if(b == -1):
        print("HaruHaru")
        exit()
    if(a[1] + b < n and b != 0):
        q.append([a[0], a[1] + b])
    if(a[0] + b < n and b != 0):
        q.append([a[0] + b, a[1]])
print("Hing")