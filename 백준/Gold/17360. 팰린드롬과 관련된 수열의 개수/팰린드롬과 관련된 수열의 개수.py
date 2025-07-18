n, m, k = map(int,input().split())
mod = 10 ** 9 + 7
if(n > k):
    if(k == 1):
        print(m ** n % mod)
    elif(k % 2 == 0):
        print(m % mod)
    else:
        print(m ** 2 % mod)
elif(n == k):
    if(k % 2 == 0):
        print(m ** (k // 2) % mod)
    else:
        print(m ** (k // 2 + 1) % mod)
else:
    print(m ** n % mod)