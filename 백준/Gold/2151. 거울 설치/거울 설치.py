import heapq, sys
input = sys.stdin.readline
n = int(input())
list1 = [[i for i in input().strip()] for _ in range(n)]
x1 = 0; y1 = 0; x2 = 0; y2 = 0
temp = 0
for i in range(n):
    for j in range(n):
        if(list1[i][j] == "#" and temp == 0):
            x1 = j; y1 = i
            temp += 1
        elif(list1[i][j] == "#" and temp == 1):
            x2 = j; y2 = i
dist_list = [[[1e99, 1e99] for _ in range(n)] for _ in range(n)] 
dist_list[y1][x1] = [0, 0]
state0 = [(1,0), (-1,0)]
state1 = [(0,1), (0,-1)]
q = [(0, 0, x1, y1), (0, 1, x1, y1)]
while q:
    dist, state, current_x, current_y = heapq.heappop(q)
    if(dist > dist_list[current_y][current_x][state]):
        continue
    if(state == 0):
        for x,y in state0:
            if(-1 < current_x + x < n and -1 < current_y + y < n and list1[current_y + y][current_x + x] != "*" and dist_list[current_y + y][current_x + x][0] > dist_list[current_y][current_x][0]):
                dist_list[current_y + y][current_x + x][0] = dist_list[current_y][current_x][0]
                heapq.heappush(q, (dist_list[current_y + y][current_x + x][0], 0, current_x + x, current_y + y))
        if(list1[current_y][current_x] == "!"):
            for x,y in state1:
                if(-1 < current_x + x < n and -1 < current_y + y < n and list1[current_y + y][current_x + x] != "*" and dist_list[current_y + y][current_x + x][1] > dist_list[current_y][current_x][0] + 1):
                    dist_list[current_y + y][current_x + x][1] = dist_list[current_y][current_x][0] + 1
                    heapq.heappush(q, (dist_list[current_y + y][current_x + x][1], 1, current_x + x, current_y + y))
    elif(state == 1):
        for x,y in state1:
            if(-1 < current_x + x < n and -1 < current_y + y < n and list1[current_y + y][current_x + x] != "*" and dist_list[current_y + y][current_x + x][1] > dist_list[current_y][current_x][1]):
                dist_list[current_y + y][current_x + x][1] = dist_list[current_y][current_x][1]
                heapq.heappush(q, (dist_list[current_y + y][current_x + x][1], 1, current_x + x, current_y + y))
        if(list1[current_y][current_x] == "!"):
            for x,y in state0:
                if(-1 < current_x + x < n and -1 < current_y + y < n and list1[current_y + y][current_x + x] != "*" and dist_list[current_y + y][current_x + x][0] > dist_list[current_y][current_x][1] + 1):
                    dist_list[current_y + y][current_x + x][0] = dist_list[current_y][current_x][1] + 1
                    heapq.heappush(q, (dist_list[current_y + y][current_x + x][0], 0, current_x + x, current_y + y))
print(min(dist_list[y2][x2]))