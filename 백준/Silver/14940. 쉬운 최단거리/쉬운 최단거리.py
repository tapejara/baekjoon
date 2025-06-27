from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
x = 0
y = 0
for i in range(n):
    for j in range(m):
        if(board[i][j] == 2):
            x = j
            y = i
            break
answer = [[0 for _ in range(m)] for _ in range(n)]
temp = deque([(x, y, 0)])
board[y][x] = 0
while temp:
    a, b, count = temp.popleft()
    count += 1
    for c, d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if(-1 < a + c < m and -1 < b + d < n and board[b + d][a + c] == 1):
            board[b + d][a + c] = 0
            answer[b + d][a + c] = count
            temp.append((a + c, b + d, count))
for i in range(n):
    for j in range(m):
        if(answer[i][j] == 0 and board[i][j] == 1):
            answer[i][j] = -1
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = " ")
    print(end = "\n")