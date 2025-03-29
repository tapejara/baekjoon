from collections import deque
import sys
input = sys.stdin.readline
a, b = map(int,input().split())
n, m = map(int,input().split())
list1 = deque([tuple(map(int,input().split())) for _ in range(m)])
q = deque([(a,0)])
while q:
    num, count = q.popleft()
    if(num == b):
        print(count)
        exit()
    temp = deque([])
    while list1:
        x, y = list1.popleft()
        if(x == num):
            q.append((y, count + 1))
        elif(y == num):
            q.append((x, count + 1))
        else:
            temp.append((x, y))
    list1 = temp.copy()
print(-1)