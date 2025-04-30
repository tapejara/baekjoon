import sys
input = sys.stdin.readline
n, m = map(int,input().split())
web = []
ps = []
for _ in range(n):
    a, b = input().strip().split()
    web.append(a)
    ps.append(b)
for _ in range(m):
    print(ps[web.index(input().strip())])