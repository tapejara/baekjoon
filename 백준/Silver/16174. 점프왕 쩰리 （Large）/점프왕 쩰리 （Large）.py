from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]
visted = [[0 for _ in range(n)] for _ in range(n)]
start = (0,0)
q = deque([start])
while q:
    a, b = q.popleft()
    c = m[a][b]
    if(c == -1):
        print("HaruHaru")
        exit()
    if(a + c < n and m[a + c][b] != 0 and visted[a + c][b] == 0):
        q.append((a + c, b))
        visted[a + c][b] = 1
    if(b + c < n and m[a][b + c] != 0 and visted[a][b + c] == 0):
        q.append((a, b + c))
        visted[a][b + c] = 1
print("Hing")