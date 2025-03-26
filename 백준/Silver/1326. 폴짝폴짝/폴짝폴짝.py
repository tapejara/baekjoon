from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
bridge = list(map(int,input().split()))
a, b = map(int,input().split())
start = (a - 1, 0)
q = deque([start])
answer = n
while q:
    flag = q.popleft()
    if(flag[0] == b - 1):
        answer = flag[1]
        break
    i = 1
    j = 1
    while(flag[0] + (bridge[flag[0]] * i) <= n - 1):
        q.append((flag[0] + (bridge[flag[0]] * i), flag[1] + 1 ))
        i += 1
    while(0 <= flag[0] - (bridge[flag[0]] * j)):
        q.append((flag[0] - (bridge[flag[0]] * j), flag[1] + 1))
        j += 1
if(answer == n or answer == 0):
    print(-1)
else:
    print(answer)