from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int,input().split()))
    point = deque([tuple(map(int,input().split())) for _ in range(n)])
    end = tuple(map(int,input().split()))
    point.append(end) 
    q = deque([start])
    result = False
    while q:
        x, y = q.popleft()
        if((x, y) == end):
            result = True
            break
        for _ in range(len(point)):
            a, b = point.popleft()
            if(abs(x - a) + abs(y - b) <= 1000):
                q.append((a, b))
            else:
                point.append((a, b))
    if(result == True):
        print("happy")
    else:
        print("sad")