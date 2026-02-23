from bisect import bisect_left
import sys
input = sys.stdin.readline
t = int(input())
for i in range(1, t + 1):
    n, k = map(int,input().split())
    a = [0] + list(map(int,input().split()))
    d = [0]
    x = [0]
    for j in range(1, n + 1):
        if(a[j] > x[-1]):
            x.append(a[j])
            d.append(len(d))
        elif(a[j] < x[-1]):
            x[bisect_left(x, a[j])] = a[j]
    print(f"Case #{i}")
    if(d[-1] >= k):
        print(1)
    else:
        print(0)