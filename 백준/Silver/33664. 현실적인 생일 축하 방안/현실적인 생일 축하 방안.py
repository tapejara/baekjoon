import sys
input = sys.stdin.readline
b, n, m = map(int,input().split())
dict = {}
for _ in range(n):
    x, y = input().split()
    dict[x] = int(y)
a = 0
for _ in range(m):
    z = input().strip()
    a += dict[z]
if(a <= b):
    print("acceptable")
else:
    print("unacceptable")