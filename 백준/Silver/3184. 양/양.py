from collections import deque
r, c = map(int,input().split())
field = [list(input()) for _ in range(r)]
q = deque([])
wolf = 0
sheep = 0
for i in range(r):
    for j in range(c):
        v = 0 
        o = 0
        if(field[i][j] != "#"):
            q.append((j, i))
            if(field[i][j] == "v"):
                v += 1
            elif(field[i][j] == "o"):
                o += 1
            field[i][j] = "#"
        while q:
            x, y = q.popleft()
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if(-1 < x + a < c and -1 < y + b < r and field[y + b][x + a] != "#"):
                    q.append((x + a, y + b))
                    if(field[y + b][x + a] == "v"):
                        v += 1
                    elif(field[y + b][x + a] == "o"):
                        o += 1
                    field[y + b][x + a] = "#"
        if(v >= o):
            o = 0
        elif(v < o):
            v = 0
        wolf += v
        sheep += o
print(sheep, wolf)