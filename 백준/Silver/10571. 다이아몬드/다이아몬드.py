import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    m = int(input())
    wc = []
    for _ in range(m):
        wc.append(list(map(float,input().split())))
    dp = [1 for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            if(wc[i][0] < wc[j][0] and wc[i][1] > wc[j][1]):
                dp[j] = max(dp[i] + 1, dp[j])
    print(max(dp))