n, m = map(int,input().split())
def function(a):
    mod = 10 ** 9 + 7
    if(a == 0):
        return 1
    elif(a % 2 == 0):
        b = function(a // 2)
        return ((b % mod) * (b % mod)) % mod
    elif(a % 2 == 1):
        b = function((a - 1) // 2)
        return ((b % mod) * (b % mod) * 2) % mod
print((function(n) + function(m) - 2) % (10 ** 9 + 7))