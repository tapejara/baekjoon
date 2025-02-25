n = int(input())
list1 = [1]
i = 2
while list1[-1] < n:
    list1.append(i ** 2)
    i += 1
dp = [i for i in range(n + 1)]
for j in range(2, n + 1):
    for element in list1:
        if(element > j):
            break
        dp[j] = min(dp[j - element] + 1, dp[j])
print(dp[n])