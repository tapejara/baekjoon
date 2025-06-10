from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, k = map(int,input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int,input().split())
        board[b][a] = 1
    bug = 0
    for i in range(n):
        for j in range(m):
            temp = deque([])
            if(board[i][j] == 1):
                bug += 1
                board[i][j] = 0
                temp.append((j, i))
            while temp:
                x, y = temp.popleft()
                for c, d in [(0,1), (0,-1), (1,0), (-1,0)]:
                    if(-1 < x + c < m and -1 < y + d < n and board[y + d][x + c] == 1):
                        temp.append((x + c, y + d))
                        board[y + d][x + c] = 0
    print(bug)                        