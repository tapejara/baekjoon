import sys 
input = sys.stdin.readline
sqaure = [i ** 2 for i in range(1,182)]
dp = [[0 for _ in range(5)] for _ in range(2 ** 15 + 1)] 
for element in sqaure:
    dp[element][1] = 1
    for j in range(element, 2 ** 15):
        dp[j][2] += dp[j - element][1]
        dp[j][3] += dp[j - element][2]
        dp[j][4] += dp[j - element][3]

while True:
    n = int(input())
    if(n == 0):
        break
    print(sum(dp[n]))