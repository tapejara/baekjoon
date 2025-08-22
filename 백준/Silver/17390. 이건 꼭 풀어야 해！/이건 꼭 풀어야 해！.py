import sys
input = sys.stdin.readline
n, q = map(int,input().split())
list1 = list(map(int,input().split()))
list1.sort()
list2 = [0]
for i in range(n):
    list2.append(list2[i] + list1[i])
for _ in range(q):
    l, r = map(int,input().split())
    print(list2[r] - list2[l - 1])