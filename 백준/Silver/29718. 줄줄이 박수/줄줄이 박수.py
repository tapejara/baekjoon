import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [0 for _ in range(m)]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(m):
        list1[j] += l[j]
a = int(input())
answer = 0
for i in range(m - a + 1):
    answer = max(answer, sum(list1[i: i + a]))
print(answer)