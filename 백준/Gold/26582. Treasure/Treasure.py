import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m, k = map(int,input().split())
    dp = [0 for _ in range(k + 1)]
    w = []
    v = []
    for _ in range(m):
        a, b = map(int,input().split())
        v.append(a)
        w.append(b)
    for i in range(m):
        for j in range(k, w[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    print(dp[k])