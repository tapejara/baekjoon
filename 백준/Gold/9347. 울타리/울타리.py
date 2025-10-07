from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    list1 = [[-1 for _ in range(m + 2)]]
    for _ in range(n):
        temp = [-1]
        for i in list(map(int,input().split())):
            temp.append(i)
        temp.append(-1)
        list1.append(temp)
    list1.append([-1 for _ in range(m + 2)])
    fence = [[1e99 for _ in range(m + 2)] for _ in range(n + 2)]
    fence[0][0] = 0
    q = deque([(0,0)])
    while q:
        current_x, current_y =q.popleft()
        for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
            if(-1 < current_x + x < m + 2 and -1 < current_y + y < n + 2 and list1[current_y + y][current_x + x] == -1 and fence[current_y + y][current_x + x] > fence[current_y][current_x]):
                fence[current_y + y][current_x + x] = fence[current_y][current_x]
                q.appendleft((current_x + x, current_y + y))
            elif(-1 < current_x + x < m + 2 and -1 < current_y + y < n + 2 and list1[current_y + y][current_x + x] == 0 and fence[current_y + y][current_x + x] > fence[current_y][current_x]):
                fence[current_y + y][current_x + x] = fence[current_y][current_x]
                q.appendleft((current_x + x, current_y + y))
            elif(-1 < current_x + x < m + 2 and -1 < current_y + y < n + 2 and list1[current_y + y][current_x + x] == 1 and fence[current_y + y][current_x + x] > fence[current_y][current_x] + 1):
                fence[current_y + y][current_x + x] = fence[current_y][current_x] + 1
                q.append((current_x + x, current_y + y))
    list2 = []
    for i in range(n + 2):
        for j in range(m + 2):
            if(list1[i][j] == 0):
                list2.append(fence[i][j])
    print(max(list2), list2.count(max(list2)))