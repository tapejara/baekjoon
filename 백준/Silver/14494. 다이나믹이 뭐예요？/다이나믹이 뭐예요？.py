n, m = map(int,input().split())
a = 10**9 + 7
board = [[1 for _ in range(n)] for _ in range(m)]
for i in range(1,m):
    for j in range(1,n):
        board[i][j] = (board[i - 1][j] % a + board[i][j - 1] % a + board[i - 1][j - 1] % a) % a
print(board[m - 1][n - 1])