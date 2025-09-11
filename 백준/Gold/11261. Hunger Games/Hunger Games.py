import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    total = int(input())
    w = list(map(int,input().split()))
    v = list(map(int,input().split()))
    dp = [0 for _ in range(total + 1)]
    for i in range(n):
        for j in range(total, w[i] - 1, -1):
            dp[j] = max(dp[j - w[i]] + v[i], dp[j])
    print(dp[total])