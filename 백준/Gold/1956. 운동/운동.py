v, e = map(int,input().split())
dist_list = [[1e99 for _ in range(v)] for _ in range(v)]
for i in range(e):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    dist_list[a][b] = min(dist_list[a][b], c)
for i in range(v):
    dist_list[i][i] = 0
    for j in range(v):
        for k in range(v):
            if(dist_list[j][k] > dist_list[j][i] + dist_list[i][k]):
                dist_list[j][k] = dist_list[j][i] + dist_list[i][k]
answer = 1e99
for i in range(v):
    for j in range(v):
        if(dist_list[i][j] == 0 or dist_list[i][j] == 1e99):
            continue
        answer = min(answer, dist_list[i][j] + dist_list[j][i])
if(answer == 1e99):
    print(-1)
else:
    print(answer)