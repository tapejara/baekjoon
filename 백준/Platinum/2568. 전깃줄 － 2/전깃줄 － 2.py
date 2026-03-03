from bisect import bisect_left
import sys
input = sys.stdin.readline
n = int(input())
a = []
b = []
c = []
for _ in range(n):
    temp = tuple(map(int,input().split()))
    a.append(temp)
    b.append(temp[0])
a.sort()
b.sort()
for i in range(n):
    c.append(a[i][1])
x = []
l = []
r = []
for y, z in a:
    i = bisect_left(x, z)
    if(i >= len(x)):
        x.append(z)
    else:
        x[i] = z
    l.append(i)
d = len(x) - 1
for j, e in enumerate(reversed(l)):
    if(e == d):
        b.remove(a[n - j - 1][0])
        d -= 1
print(len(b))
for num in b:
    print(num)