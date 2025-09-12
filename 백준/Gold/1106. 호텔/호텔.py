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
    for j in range(w[i],c + max(w) + 1):
            dp[j] = min(dp[j], dp[j - w[i]] + v[i])
print(min(dp[c:-1]))