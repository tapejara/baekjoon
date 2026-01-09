import sys
input = sys.stdin.readline
list1 = [{} for _ in range(200001)]
n, m, q = map(int,input().split())
for _ in range(m):
    a, b, c = map(int,input().split())
    if(b in list1[a]):
        list1[a][b] = min(list1[a][b], c)
        list1[b][a] = min(list1[b][a], c)
    else:
        list1[a][b] = c
        list1[b][a] = c
for _ in range(q):
    s, e = map(int,input().split())
    try:
        print(list1[s][e])
    except:
        print(-1)