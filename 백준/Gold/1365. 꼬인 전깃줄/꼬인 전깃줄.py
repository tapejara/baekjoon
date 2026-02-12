from bisect import bisect_left
n = int(input())
a = [0] + list(map(int,input().split()))
d = [0]
x = [0]
for i in range(1, n + 1):
    if(a[i] > x[-1]):
        x.append(a[i])
        d.append(len(d))
    elif(a[i] < x[-1]):
        x[bisect_left(x, a[i])] = a[i]
print(n - d[-1])