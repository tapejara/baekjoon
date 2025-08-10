from itertools import product
r, c, h = map(int,input().split())
cube = [[[i for i in input()] for _ in range(r)] for _ in range(h)]
answer = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(h)]
space = list(product([1,-1,0], repeat = 3))
for i in range(h):
    for j in range(r):
        for k in range(c):
            if(cube[i][j][k] == "*"):
                answer[i][j][k] = "*"
            else:
                for x, y, z in space:
                    if(-1 < i + z < h and -1 < j + y < r and -1 < k + x < c and cube[i + z][j + y][k + x] == "*"):
                        answer[i][j][k] += 1
for i in range(h):
    for j in range(r):
        for k in range(c):
            if(k == c - 1):
                if(answer[i][j][k] == "*"):
                    print(answer[i][j][k])
                else:
                    print(answer[i][j][k] % 10)
            else:
                if(answer[i][j][k] == "*"):
                    print(answer[i][j][k], end="")
                else:
                    print(answer[i][j][k] % 10, end="")