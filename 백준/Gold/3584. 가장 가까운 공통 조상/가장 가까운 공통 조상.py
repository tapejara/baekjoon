import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
def dfs(node):
        if(list1[node] in set1):
            print(list1[node])
        elif(list1[node] != 0):
            set1.add(list1[node])
            dfs(list1[node])
for _ in range(t):
    n = int(input())
    list1 = [0 for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = map(int,input().split())
        list1[b] = a
    x, y = map(int,input().split())
    set1 = set({x,y})
    dfs(x)
    dfs(y)