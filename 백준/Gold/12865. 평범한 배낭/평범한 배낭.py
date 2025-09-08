import sys
input = sys.stdin.readline
n, k = map(int,input().split())
list1 = [(0, 0)] + [tuple(map(int,input().split())) for _ in range(n)]
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(1, k + 1):
        if(j - list1[i][0] >= 0):
            dp[i][j] = max(dp[i - 1][j - list1[i][0]] + list1[i][1], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][k])