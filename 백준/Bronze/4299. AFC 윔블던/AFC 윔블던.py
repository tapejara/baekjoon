n, m = map(int,input().split())
if((n - m) % 2 != 0 or n < m):
    print(-1)
else:
    a = (n - m) // 2
    print(a + m, a)