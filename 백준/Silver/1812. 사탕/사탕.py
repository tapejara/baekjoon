import sys
input = sys.stdin.readline
n = int(input())
list1 = [int(input()) for _ in range(n)]
answer = []
start = 0
for i in range(n):
    if(i % 2 == 0):
        start += list1[i]
    else:
        start -= list1[i]
start //= 2
answer.append(start)
for i in range(n):
    answer.append(list1[i] - start)
    start = list1[i] - start
for i in range(n):
    print(answer[i])