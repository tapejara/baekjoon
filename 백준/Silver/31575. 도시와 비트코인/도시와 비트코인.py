from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(m)]
start = (0,0)
q = deque([start])
while q:
    a = q.popleft()
    if(a == (n - 1, m - 1)):
        print("Yes")
        exit()
    if(a[1] + 1 < m):
        if(city[a[1] + 1][a[0]] == 1 and not (a[0], a[1] + 1) in q):
            q.append((a[0], a[1] + 1))
    if(a[0] + 1 < n):
        if(a[0] < n and city[a[1]][a[0] + 1] == 1 and not (a[0] + 1,a[1]) in q):
            q.append((a[0] + 1,a[1]))
print("No")