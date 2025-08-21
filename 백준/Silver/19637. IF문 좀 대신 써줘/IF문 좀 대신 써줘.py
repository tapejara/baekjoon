from bisect import bisect_left
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = []
list2 = []
for _ in range(n):
    a, b = input().split()
    list1.append(a)
    list2.append(int(b))
list3 = [int(input()) for _ in range(m)]
for i in range(m):
    print(list1[bisect_left(list2, list3[i])])