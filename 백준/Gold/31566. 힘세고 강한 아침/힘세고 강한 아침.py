import sys
input = sys.stdin.readline
def function():
    n, m, q = map(int,input().split())
    dist = [[[10 ** 30] * n for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        b, t, c = map(int,input().split())
        b -= 1; t -= 1
        for j in range(n):
            if(b == j or t == j):
                continue
            else:
                dist[j][b][t] = c
    for h in range(n):
        for i in range(n):
            if(i == h):
                continue
            else:
                dist[h][i][i] = 0
                for j in range(n):
                    if(j == h):
                        continue
                    for k in range(n):
                        if(k == h):
                            continue
                        dist[h][j][k] = min(dist[h][j][i] + dist[h][i][k], dist[h][j][k])
    for _ in range(q):  
        s, k, e = map(int,input().split())
        s -= 1; k -= 1; e -= 1
        if(dist[k][s][e] == 10 ** 30):
            print("No")
        else:    
            print(dist[k][s][e])
function()