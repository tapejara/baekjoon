import sys
input = sys.stdin.readline
a,b = map(int,input().split())
list = []
for _ in range(a):
    list.append(0)
for _ in range(b):
    c,d,e = map(int,input().split())
    for i in range(c-1,d):
        list[i] = e
for element in list:
    print(element,end=' ')