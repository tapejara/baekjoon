import sys
input = sys.stdin.readline
n, m, a, b = map(int,input().split())
item = [(0,0),(n - 1, m - 1)]
barrier = set()
for _ in range(a):
    x, y = map(int,input().split())
    item.append((x - 1, y - 1))
for _ in range(b):
    x, y = map(int,input().split())
    barrier.add((x - 1, y - 1))
item.sort(key=lambda x: (x[0], x[1]))
board = [[0] * n for _ in range(m)]
board[0][0] = 1
for i in range(len(item) - 1):
    x1, y1 = item[i]
    x2, y2 = item[i + 1]
    for j in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            if(j == x1 and k == y1):
                continue
            elif((j, k) in barrier):
                board[k][j] == 0
            elif(k == 0):
                board[k][j] = board[k][j - 1]
            elif(j == 0):
                board[k][j] = board[k - 1][j]
            else:
                board[k][j] = board[k - 1][j] + board[k][j - 1]
print(board[-1][-1])