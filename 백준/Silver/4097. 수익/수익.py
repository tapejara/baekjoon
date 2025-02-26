import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if(n == 0):
        break
    list1 = []
    for _ in range(n):
        list1.append(int(input()))
    dp = [list1[0]]
    for i in range(1,n):
        if(dp[i - 1] + list1[i] > list1[i]):
            dp.append(dp[i - 1] + list1[i])
        else:
            dp.append(list1[i])
    print(max(dp))