from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
r1, c1, r2, c2 = map(int,input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
q = deque([(r1, c1, 0)])
while q:
    r, c, count  = q.popleft()
    if(r == r2 and c == c2):
        print(count)
        exit()
    shift = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    for a,b in shift:
        if(-1 < r + a < n and -1 < c + b < n and board[c + b][r + a] == 0):
            q.append((r + a, c + b, count + 1))
            board[c + b][r + a] = 1
print(-1)