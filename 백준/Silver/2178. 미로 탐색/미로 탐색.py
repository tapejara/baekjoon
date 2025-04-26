from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
board = [[int(i) for i in input().strip()] for _ in range(n)]
board[0][0] = 0
start =(0,0,1)
q = deque([start])
while q:
    x, y, c = q.popleft()
    if(x == m - 1 and y == n - 1):
        print(c)
        exit()
    for a,b in [(1,0), (-1,0), (0,1), (0,-1)]:
        if(-1 < x + a < m and -1 < y + b < n and board[y + b][x + a] == 1):
            q.append((x + a, y + b, c + 1)) 
            board[y + b][x + a] = 0