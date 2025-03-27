from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
bridge = list(map(int,input().split()))
a, b = map(int,input().split())
a -= 1
b -= 1
start = (a, 0)
q = deque([start])
answer = n
while q:
    flag = q.popleft()
    if(flag[0] == b):
        answer = flag[1]
        break
    jump = bridge[flag[0]]
    for i in range(flag[0] + jump, n, jump):
        q.append((i, flag[1] + 1))
    for i in range(flag[0] - jump, -1, -jump):
        q.append((i, flag[1] + 1))
if(answer == n or answer == 0):
    print(-1)
else:
    print(answer)