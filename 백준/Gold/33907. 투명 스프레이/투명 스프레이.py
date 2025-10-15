from collections import deque
import sys
input = sys.stdin.readline
n, m, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
def function(x):
    dist = [[1e99 for _ in range(m)] for _ in range(n)]
    dist[0][0] = 0
    q = deque([(0, 0)])
    while q:
        current_x, current_y = q.popleft()
        for a,b in [(1,0), (-1,0), (0,1), (0,-1)]:
            if(-1 < current_x + a < m and -1 < current_y + b < n):
                if(board[current_y + b][current_x + a] > x and dist[current_y + b][current_x + a] > dist[current_y][current_x] + 1 and k >= dist[current_y][current_x] + 1):
                    dist[current_y + b][current_x + a] = dist[current_y][current_x] + 1
                    q.append((current_x + a, current_y + b))
                elif(board[current_y + b][current_x + a] <= x and dist[current_y + b][current_x + a] > dist[current_y][current_x] and k >= dist[current_y][current_x]):
                    dist[current_y + b][current_x + a] = dist[current_y][current_x]
                    q.appendleft((current_x + a, current_y + b))    
    return dist[-1][-1]
minimum, maximum = 0, 10**9
answer = -1 
while minimum <= maximum:
    mid = (minimum + maximum) // 2
    if function(mid) <= k:
        answer = mid
        maximum = mid - 1
    else:
        minimum = mid + 1
print(answer)
