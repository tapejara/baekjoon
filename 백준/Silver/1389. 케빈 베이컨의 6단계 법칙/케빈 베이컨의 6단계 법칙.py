n, m = map(int,input().split())
dist_list = [[1e99 for _ in range(n)] for _ in range(n)]
for _ in range(m): 
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    dist_list[a][b] = min(dist_list[a][b], 1)
    dist_list[b][a] = min(dist_list[a][b], 1)
for i in range(n):
    dist_list[i][i] = 0
    for j in range(n):
        for k in range(n):
            if(dist_list[j][k] > dist_list[j][i] + dist_list[i][k]):
                dist_list[j][k] = dist_list[j][i] + dist_list[i][k]
temp = 1e99
answer = 0
for i in range(n):
    if(sum(dist_list[i]) < temp):
        temp = sum(dist_list[i])
        answer = i
print(answer + 1)