import sys
input = sys.stdin.readline
n, k = map(int,input().split())
c = list(map(int,input().split()))
c.sort()
dp = [1e9 for _ in range(k + 1)]
dp[0] = 0
for i in range(n):
    for j in range(k, c[i] - 1, -1):
        if(dp[j - c[i] != 1e9]):
            dp[j] = min(dp[j], dp[j - c[i]] + 1)
if(dp[k] != 1e9):
    print(dp[k])
else:
    print(-1)