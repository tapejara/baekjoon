n = int(input())
list1 = [0] + list(map(int,input().split()))
list2 = [0] + list(map(int,input().split()))
dp = [[0 for _ in range(100)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1,100):
        if(j - list1[i] >= 0):
            dp[i][j] = max(list2[i] + dp[i - 1][j - list1[i]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n][99])