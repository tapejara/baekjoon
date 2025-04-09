import sys
input = sys.stdin.readline
board = [list(map(int,input().split())) for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
r, c = map(int,input().split())
flag = board[r][c]
apple = board[r][c]
distance = 0
def dfs(y, x, d):
    global apple
    if(apple >= 2):
        print(1)
        exit()
    visited[y][x] = -1
    for a,b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if(-1 < y + a < 5 and -1 < x + b < 5 and board[y + a][x + b] != -1 and d < 3 and visited[y + a][x + b] != -1):
            if(apple >= 1 and y == r and x ==c):
                apple = flag
            if(board[y + a][x + b] == 1):
                apple += 1
            visited[y + a][x + b] = -1
            dfs(y + a, x + b, d + 1)
            visited[y + a][x + b] = 0
    return 0
print(dfs(r, c, distance))