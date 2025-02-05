import sys
input = sys.stdin.readline
n = int(input())
list_a = list(map(int,input().split()))
list_a.sort()
list1 = []
list2 = []
for i in range(n - 1):
    b = (list_a[i] + list_a[i + 1]) // 2
    if(not b in list_a):
        list1.append(b)
        list2.append(b - list_a[i])
if(len(list1) == 0):
    print(-1)
else:
    print(list1[list2.index(max(list2))])