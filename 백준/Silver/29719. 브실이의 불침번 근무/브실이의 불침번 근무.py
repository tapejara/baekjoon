n, m = map(int,input().split())
mod = 1000000007
total = (m ** n) % mod
exception = ((m - 1) ** n) % mod
print((total - exception)% mod)