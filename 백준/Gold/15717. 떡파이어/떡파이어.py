n = int(input())
mod = 10**9 + 7
def function(x):
    global mod
    if(x == 0):
        return 1
    elif(x % 2 == 0):
        a = function(x // 2)
        return ((a % mod) * (a % mod)) % mod
    elif(x % 2 == 1):
        a = function((x - 1) // 2)
        return ((a % mod) * (a % mod) * 2) % mod
if(n == 0):
    print(1)
else:
    print(function(n - 1))