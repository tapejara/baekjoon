import sys
input = sys.stdin.readline
m, n = map(int,input().split())
f = [list(map(int,input().split())) for _ in range(m)]
b = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if(f[i][j] == 1 or f[i][j] == 2):
              b[i][j] = -1
        else:
            if(i == 0 or j == 0):
                b[i][j] = 1
for i in range(1, m):
    for j in range(1, n):
        if(b[i][j] == -1):
            continue
        elif(b[i - 1][j - 1] == -1 or b[i][j - 1] == -1 or b[i - 1][j] == -1):
            b[i][j] = 1
        else:
            b[i][j] = min(b[i - 1][j - 1], b[i][j - 1], b[i - 1][j]) + 1
answer = 0
for i in range(m):
    for j in range(n):
        answer = max(answer, b[i][j])      
print(answer)