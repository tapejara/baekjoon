import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
dps = [int(input()) for _ in range(n)]
list1 = [(0,0)] + [tuple(map(int,input().split())) for _ in range(k)]
dps.sort(reverse=True)
answer = 0
for i in range(m):
    dp = [[0 for _ in range(901)] for _ in range(k + 1)]
    t = []
    for element in list1:
        if(element[0] % dps[i] == 0):
            t.append(element[0] // dps[i])
        else:
            t.append(element[0] // dps[i] + 1)
    for j in range(1, k + 1):
        for l in range(1, 901):
            if(l - t[j] >= 0):
                dp[j][l] = max(dp[j - 1][l - t[j]] + list1[j][1], dp[j - 1][l])
            else:
                dp[j][l] = dp[j - 1][l]
    answer += dp[-1][-1]
print(answer)