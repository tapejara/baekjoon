import sys
input = sys.stdin.readline
n = int(input())
list1 = list(tuple(map(int,input().split())) for _ in range(n))
answer = 0
flag = list1.pop()
for i in range(n - 1):
    a, b = list1.pop()
    answer += a * flag[0] * flag[1]
    flag = (a,flag[1])
print(answer)