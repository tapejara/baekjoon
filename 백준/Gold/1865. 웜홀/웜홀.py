import sys
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    n, m, w = map(int,input().split())
    list1 = []
    for _ in range(m):
        s, e, t = map(int,input().split())
        list1.append((s, e, t))
        list1.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int,input().split())
        list1.append((s, e, -1 * t))
    dist_list = [1e99 for _ in range(n + 1)]
    answer = False
    for i in range(1, n + 1):
        if(dist_list[i] == 1e99):
            dist_list[i] = 0
            for j in range(n):
                for k in range(len(list1)):
                    a, b, c = list1[k]
                    if(dist_list[a] != 1e99 and dist_list[b] > dist_list[a] + c):
                        dist_list[b] = dist_list[a] + c
                        if(j == n - 1):
                            answer = True
                            break
        if(answer == True):
            break
    if(answer == True):
        print("YES")
    elif(answer == False):
        print("NO")