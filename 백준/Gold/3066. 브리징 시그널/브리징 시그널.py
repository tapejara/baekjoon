from bisect import bisect_left
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = [0]
    for _ in range(n):
        a.append(int(input()))
    d = [0]
    x = [0]
    for i in range(1, n + 1):
        if(a[i] > x[-1]):
            x.append(a[i])
            d.append(len(d))
        elif(a[i] < x[-1]):
            x[bisect_left(x, a[i])] = a[i]
    print(d[-1])