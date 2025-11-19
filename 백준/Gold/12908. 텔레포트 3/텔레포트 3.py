list1 = []
for _ in range(2):
    list1.append(tuple(map(int,input().split())))
dist_list = [[1e99 for _ in range(8)] for _ in range(8)]
for _ in range(3):
    x1, y1, x2, y2 = map(int,input().split())
    list1.append((x1, y1))
    list1.append((x2, y2))
for i in range(8):
    dist_list[i][i] = 0
    for j in range(8):
        dist_list[i][j] = min(dist_list[i][j], (abs(list1[i][0] - list1[j][0]) + abs(list1[i][1] - list1[j][1])))
for i in range(2,8,2):
    dist_list[i][i + 1] = min(dist_list[i][i + 1], 10)
    dist_list[i + 1][i] = min(dist_list[i + 1][i], 10)
for i in range(8):
    for j in range(8):
        for k in range(8):
            if(dist_list[j][k] > dist_list[j][i] + dist_list[i][k]):
                dist_list[j][k] = dist_list[j][i] + dist_list[i][k]
print(dist_list[0][1])