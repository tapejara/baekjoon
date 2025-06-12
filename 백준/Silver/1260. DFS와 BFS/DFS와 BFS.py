from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int,input().split())
list1 = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int,input().split())
    list1[a].append(b)
    list1[b].append(a)
for i in range(n + 1):
    list1[i].sort()
list_bfs = [0 for _ in range(n + 1)]
list_dfs = [0 for _ in range(n + 1)]
def function(x):
    list_dfs[x] = 1
    print(x, end=" ")
    for element in list1[x]:
        if(list_dfs[element] == 0):
            function(element)
function(v)
print(end="\n")
temp = deque([v])
list_bfs[v] = 1
while temp:
    c = temp.popleft()
    print(c, end=" ")
    for element in list1[c]:
        if(list_bfs[element] == 0):
            list_bfs[element] = 1
            temp.append(element)