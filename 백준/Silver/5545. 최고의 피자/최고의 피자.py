import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int,input().split())
c = int(input())
list1 = [int(input()) for _ in range(n)]
list1.sort(reverse = True)
answer = c // a
temp = c
for i in range(n):
    temp += list1[i]
    answer = max(answer, temp // (a + b * (i + 1)))
print(answer)