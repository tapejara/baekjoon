import sys
input = sys.stdin.readline
c, n = map(int,input().split())
v = []
w = []
for _ in range(n):
    a, b = map(int,input().split())
    v.append(a)
    w.append(b)
dp = [1e9 for _ in range(c + max(w) + 1)]
dp[0] = 0
count = c // min(w) + 1
for i in range(n):
    for j in range(count):
        for l in range(c + max(w), w[i] - 1, -1):
            dp[l] = min(dp[l], dp[l - w[i]] + v[i])
print(min(dp[c:-1]))