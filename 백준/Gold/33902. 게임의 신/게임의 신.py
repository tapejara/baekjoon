x, y = map(int,input().split())
game = [i for i in range(x, y)]
game.sort(reverse = True)
dp = [0 for _ in range(x, y)]
for i in range(y - x):
    a = y
    b = game[i]
    while b != 0:
        a, b = b, a % b
    if(a == 1):
        dp[i] = 1
for i in range(1, y - x):
    if(dp[i] == 1):
        continue
    for j in range(i):
        c = game[i]
        d = game[j]
        while d != 0:
            c, d = d, c % d
        if(c == 1 and dp[j] == 0):
            dp[i] = 1
if(dp[-1] == 1):
    print("khj20006")
else:
    print("putdata")