import sys
input = sys.stdin.readline
n = int(input())
list1 = list(map(int,input().split()))
list2 = [0]
for i in range(n):
    list2.append(list1[i] + list2[-1])
m = int(input())
for _ in range(m):
    a, b = map(int,input().split())
    print(list2[b] - list2[a - 1])