import sys
input= sys.stdin.readline
t = int(input())
for _ in range(t):
    h, w = map(int,input().split())
    field = [[c for c in input()] for _ in range(h)]
    count = [[0 for _ in range(w)] for _ in range(h)]
    q = []
    answer = 0
    for i in range(h):
        for j in range(w):
            if(field[i][j] == "#" and count[i][j] == 0):
                q.append((j,i))
                count[i][j] = 1
                answer += 1
                while q:
                    point = q.pop(0)
                    pj = point[0]
                    pi = point[1]
                    if(pi + 1 < h ):
                        if(field[pi + 1][pj] == "#" and count[pi + 1][pj] == 0):
                            q.append((pj, pi + 1))
                            count[pi + 1][pj] = 1
                    if(pi - 1 > -1 ):
                        if(field[pi - 1][pj] == "#" and count[pi - 1][pj] == 0):
                            q.append((pj, pi - 1))
                            count[pi - 1][pj] = 1
                    if(pj + 1 < w):
                        if(field[pi][pj + 1] == "#" and count[pi][pj + 1] == 0):
                            q.append((pj + 1, pi))
                            count[pi][pj + 1] = 1
                    if(pj -1 > -1):
                        if(field[pi][pj - 1] == "#" and count[pi][pj - 1] == 0):
                            q.append((pj - 1, pi))
                            count[pi][pj - 1] = 1
    print(answer)