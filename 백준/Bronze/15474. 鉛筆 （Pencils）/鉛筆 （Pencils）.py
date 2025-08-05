n, a, b, c, d = map(int,input().split())
a1 = n // a
c1 = n // c
if(n % a != 0):
    a1 += 1
if(n % c != 0):
    c1 += 1
print(min(a1 * b, c1 * d))