import sys
input = sys.stdin.readline
a,b = map(int,input().split())
list = []
for i in range(1,a+1):
    list.append(i)
for i in range(b):
    c,d = map(int,input().split())
    e = list[c - 1]
    f = list[d - 1]
    list[c - 1] = f
    list[d - 1] = e
for element in list:
    print(element,end=' ')