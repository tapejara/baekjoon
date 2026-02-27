from bisect import bisect_left
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    x = []
    l = []
    r = []
    for num in a:
        i = bisect_left(x, num)
        if(i >= len(x)):
            x.append(num)
        else:
            x[i] = num
        l.append(i)
    b = len(x) - 1
    for j, e in enumerate(reversed(l)):
        if(e == b):
            r.append(n - j)
            b -= 1
    print(len(x))
    for num in reversed(r):
        print(num, end = " ")
    print()