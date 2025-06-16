from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
board = [[i for i in input().strip()] for _ in range(n)]
start = [0,0]
answer = 0
for i in range(n):
    for j in range(m):
        if(board[i][j] == "I"):
            start = [j, i]
            board[i][j] = "X"
temp = deque([start])
while temp:
    x, y = temp.popleft()
    for a, b in [(1,0), (-1,0), (0,1), (0,-1)]:
        if(-1 < x + a < m and -1 < y + b < n and board[y + b][x + a] != "X"):
            if(board[y + b][x + a] == "P"):
                answer += 1
            board[y + b][x + a] = "X"
            temp.append((x + a, y + b))
if(answer == 0):
    print("TT")
else:
    print(answer)