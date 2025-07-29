from collections import deque
import sys
input = sys.stdin.readline
n, m =map(int,input().split())
maze  = [[i for i in input().strip()] for _ in range(n)]
start = deque([])
friends = []
gate =[]
for i in range(n):
    for j in range(m):
        if(maze[i][j] == "H"):
            start.append((j, i, 0))
        elif(maze[i][j] == "P"):
            friends.append((j, i, 0))
        elif(maze[i][j] == "#"):
            gate.append((j,i))
end = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(len(friends) + 1)]
def bfs(space, dq, num):
    space[dq[0][1]][dq[0][0]] = "X"
    while dq:
        x, y, c = dq.popleft()
        for a, b in [(0,1), (0,-1), (1,0), (-1,0)]:
            if(-1 < x + a < m and -1 < y + b < n and space[y + b][x + a] != "X"):
                if(space[y + b][x + a] == "#"):
                    space[y + b][x + a] = "X"
                    end[num][y + b][x + a] = c + 1
                    dq.append((x + a, y + b, c + 1))
                else:
                    space[y + b][x + a] = "X"
                    dq.append((x + a, y + b, c + 1))
board1 = [maze[i].copy() for i in range(n)]
bfs(board1, start, 0)
for i in range(len(friends)):
    temp = deque([friends[i]])
    board2 = [maze[j].copy() for j in range(n)]
    bfs(board2, temp, i + 1)
answer = []
for element in gate:
    x, y = element
    count = 0
    for i in range(1, len(friends) + 1):
        if(end[0][y][x] >= end[i][y][x] and end[i][y][x] != 0):
            count += 1
    answer.append(count)
print(max(answer))