import sys
input = sys.stdin.readline
n,m = map(int,input().split())
list1 = [list(map(int,input().split())) for _ in range(n)]
for i in range(n - 1):
    for j in range(m):
        list2 = list1[i][:j] + list1[i][j + 1:]
        list1[i + 1][j] += min(list2)
print(min(list1[n - 1]))