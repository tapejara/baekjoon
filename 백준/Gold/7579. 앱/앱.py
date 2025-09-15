import sys
input = sys.stdin.readline
n, m = map(int,input().split())
v = list(map(int,input().split()))
w = list(map(int,input().split()))
dp = [0 for _ in range(sum(w) + 1)]
for i in range(n):
    for j in range(sum(w), w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])
for i in range(sum(w) + 1):
    if(dp[i] >= m):
        print(i)
        break