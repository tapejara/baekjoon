import sys
input = sys.stdin.readline
n, m = map(int,input().split())
dic1 = {}
dic2 = {}
for i in range(1, n + 1):
    c = input().strip()
    dic1[i] = c
    dic2[c] = i
for i in range(m):
    d = input().strip()
    if(d in dic2):
        print(dic2[d])
    else:
        print(dic1[int(d)])