import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
board = [list(input().split()) for _ in range(5)]
answer = set()
temp = []

def dfs(y, x):
    temp.append(board[y][x])
    if(len(temp) == 6):
        num = ""
        for c in temp:
            num += c
        answer.add(num)
    for a,b in [(1,0), (-1,0), (0,1), (0,-1)]:
        if(-1 < y + a < 5 and -1 < x + b < 5 and len(temp) < 6):
            dfs(y + a, x + b)
            temp.pop()

for i in range(5):
    for j in range(5):
        dfs(i,j)
        temp.clear()
print(len(answer))