import sys
input = sys.stdin.readline
a,b = map(int,input().split())
list = list(map(int, input().split()))
for element in list:
    if(element < b):
        print(element,end=' ')