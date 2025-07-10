import sys
input = sys.stdin.readline
n = int(input())
list1 = [list(map(int,input().split())) for _ in range(n)]
for i in range(n - 1):
    for j in range(3):
        list1[i + 1][j] += min(list1[i][:j] + list1[i][j+ 1:])
print(min(list1[n - 1]))