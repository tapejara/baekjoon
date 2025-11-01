import sys
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [tuple(map(int,input().split())) for _ in range(m)]
dist_list = [1e99 for _ in range(n + 1)]
dist_list[1] = 0
for i in range(n):
    for j in range(m):
        a, b, c = list1[j]
        if(dist_list[a] != 1e99 and dist_list[b] > dist_list[a] + c):
           dist_list[b] = dist_list[a] + c 
           if(i == n - 1):
              print(-1)
              exit()
for i in range(2, n + 1):
    if(dist_list[i] == 1e99):
        print(-1)
    else:
        print(dist_list[i])