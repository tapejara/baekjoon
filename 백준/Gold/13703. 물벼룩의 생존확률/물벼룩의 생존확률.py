k, n = map(int,input().split())
if(k == 0):
    print(0)
    exit()
dp = [[0 for _ in range(127)]]
dp[0][k] = 1
for i in range(1, n + 1):
    temp = [0 for _ in range(127)]
    for j in range(1,127):
        temp[j - 1] += dp[i - 1][j]
        if(j + 1 < 127):
            temp[j + 1] += dp[i - 1][j]
    dp.append(temp)
answer = dp[-1][1:]
print(sum(answer))