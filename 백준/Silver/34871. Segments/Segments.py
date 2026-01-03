import sys
input = sys.stdin.readline
n, q = map(int,input().split())
max_l = 0
min_r = 10 ** 9 + 1
for _ in range(n):
    l, r, y = map(int,input().split())
    max_l = max(l, max_l)
    min_r = min(r, min_r)
for _ in range(q):
    p = int(input())
    if(max(max_l - p, p -min_r) < 0):
        print(0)
    else:
        print(max(max_l - p, p -min_r))