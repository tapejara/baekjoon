n, m, k = map(int,input().split())
x1 = n - m
x2 = n - k
print((max(m,k) - abs(m - k)) + (max(x1, x2) - abs(x1 - x2)))