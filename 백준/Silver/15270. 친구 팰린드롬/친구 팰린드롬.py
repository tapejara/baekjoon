import sys
input = sys.stdin.readline
n, m = map(int,input().split())
connection = [[] for _ in range(n)]
dancer = [0 for _ in range(n)]
for _ in range(m):
    a, b = map(int,input().split())
    connection[a - 1].append(b - 1)
    connection[b - 1].append(a - 1)
answer = []
def dfs(x, y):
    global answer
    if(x == n - 1):
        if(0 in dancer):
            answer.append(y + 1)
        else:
            answer.append(y)
    elif(dancer[x] == 1):
        dfs(x + 1, y)
    else:
        for element in connection[x]:
            if(dancer[element] == 0):
                dancer[x] = 1
                dancer[element] = 1
                dfs(x + 1, y + 2)
                dancer[x] = 0
                dancer[element] = 0
        dfs(x + 1, y)
dfs(0,0)
print(max(answer))