import sys
input = sys.stdin.readline
n, k = map(int,input().split())
list1 = [[0,0]] + [list(map(int,input().split())) for _ in range(k)]
board = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
for i in range(1, k + 1):
    for j in range(1, n + 1):
        if(j < list1[i][1]):
            board[i][j] = board[i - 1][j]
        else:
            board[i][j] = max(board[i - 1][j - list1[i][1]] + list1[i][0], board[i - 1][j])
print(board[k][n])