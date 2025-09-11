import sys
input = sys.stdin.readline
c, m = map(int,input().split())
list1 = [[0] + list(map(int,input().split())) for _ in range(m)]
dp = [0 for _ in range(c + 1)]
origin = dp.copy()
for i in range(m):
    for j in range(c + 1):
        for l in range(c, j - 1, -1):
            dp[l] = max(origin[l - j] + list1[i][j], dp[l])
    origin = dp.copy()
print(dp[c])