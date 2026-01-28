import sys
input = sys.stdin.readline
mod = 10**9 + 7
def function(x):
    global mod
    if(x == 0):
        return 1
    elif(x % 2 == 0):
        temp = function(x // 2)
        return ((temp % mod) * (temp % mod)) % mod
    elif(x % 2 == 1):
        temp = function((x - 1) // 2)
        return ((temp % mod) * (temp % mod) * 2) % mod
t = int(input())
for _ in range(t):
    n = int(input())
    if(n == 1):
        print(1)
    else:
        print(function(n - 2))