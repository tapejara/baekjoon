import sys
input = sys.stdin.readline
a = int(input())
for i in range(a):
    list1= list(map(int,input().split()))
    print(min(list1))