from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
dq = deque([tuple(map(int,input().split())) for _ in range(n - 1)])
q = deque([(1, 0)])
answer = []
while q:
    room, length = q.popleft()
    answer.append(length)
    temp = deque([])
    while dq:
        a, b, c = dq.popleft()
        if(room == a):
            q.append((b, length + c))
        elif(room == b):
            q.append((a, length + c))
        else:
            temp.append((a, b, c))
    dq = temp.copy()
print(max(answer))