import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(m + 1)]
h = []
f = []
for _ in range(n):
    x, y = map(int,input().split())
    h.append(x)
    f.append(y)
for i in range(n):
    for j in range(m, h[i] - 1, -1):
        for l in range(k, f[i] - 1, -1):
            dp[j][l] = max(dp[j][l], dp[j - h[i]][l - f[i]] + 1)
print(dp[m][k])