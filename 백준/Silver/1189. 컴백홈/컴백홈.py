r, c, k = map(int,input().split())
board = [[i for i in input()] for _ in range(r)]
count = 0
board[r - 1][0] = "T"

def dfs(x, y , d):
    global count
    if(d == k and x == c - 1 and y == 0):
        count += 1
        return
    for a,b in [(1,0), (-1,0), (0,1), (0,-1)]:
        if(-1 < x + a < c and -1 < y + b < r and board[y + b][x + a] != "T"):
            board[y + b][x + a] = "T"
            dfs(x + a, y + b, d + 1)
            board[y + b][x + a] = "."

dfs(0, r - 1, 1)
print(count)