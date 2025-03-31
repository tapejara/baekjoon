from collections import deque
import sys
input= sys.stdin.readline
t = int(input())
for _ in range(t):
    l = int(input())
    start_a, start_b = map(int,input().split())
    end_a, end_b = map(int,input().split())
    board = [[0 for _ in range(l)] for _ in range(l)]
    q = deque([(start_a, start_b, 0)])
    while q:
        point_a, point_b, count = q.popleft()
        if(point_a == end_a and point_b == end_b):
            print(count)
            break
        shift =[(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
        for a,b in shift:
            if(-1 < point_a + a < l and -1 < point_b + b < l and board[point_a + a][point_b + b] == 0):
                q.append((point_a + a, point_b + b , count + 1))
                board[point_a + a][point_b + b] = 1