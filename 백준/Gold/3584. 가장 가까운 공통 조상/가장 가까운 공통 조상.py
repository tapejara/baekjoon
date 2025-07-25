import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    list1 = [tuple(map(int,input().split())) for _ in range(n - 1)]
    x, y = map(int,input().split())
    list_x = [x,y]
    def dfs(node):
        for i in range(n - 1):
            if(list1[i][1] == node):
                if(list1[i][0] in list_x):
                    print(list1[i][0])
                else:
                    list_x.append(list1[i][0])
                    dfs(list1[i][0])
    dfs(x)
    dfs(y)