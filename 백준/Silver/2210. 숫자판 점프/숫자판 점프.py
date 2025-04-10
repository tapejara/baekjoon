board = [list(input().split()) for _ in range(5)]
answer = set()

def dfs(y, x, t):
    if(len(t) == 6):
        answer.add(t)
    for a,b in [(1,0), (-1,0), (0,1), (0,-1)]:
        if(-1 < y + a < 5 and -1 < x + b < 5 and len(t) < 6):
            dfs(y + a, x + b, t + board[y + a][x + b])

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])
        
print(len(answer))