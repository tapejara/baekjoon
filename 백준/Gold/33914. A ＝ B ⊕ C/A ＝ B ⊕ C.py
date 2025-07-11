import math
x, y = map(int,input().split())
mod = 10 ** 9 + 7
a = 3 ** (x // 2) % mod
b = (y - x // 2) // 3
c = max(x // 2, b)
d = min(x // 2, b)
if(x % 2 != 0):
    print(0)
elif(y - (x // 2) < 0):
    print(0)
elif(y - (x // 2) == 0):
    print(a)
else:
    print((a * (math.comb(c + d, d) % mod)) % mod)