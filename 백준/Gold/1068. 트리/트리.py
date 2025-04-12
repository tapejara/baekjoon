n = int(input())
list1 = list(map(int,input().split()))
m = int(input())
tree = [[] for _ in range(n)]
for i in range(n):
    if(list1[i] != -1):
        tree[list1[i]].append(i)
tree[m].append(-1)
visited = []
count = 0

def dfs(t,f):
    global count
    if(len(t) == 0 and f == 0):
        count += 1
    elif(len(t) == 1 and f == 0 and m in t):
        count += 1
    if(-1 not in t):
        for element in t:
            visited.append(element)
            dfs(tree[element],f)
    elif(-1 in t):
        for element in t:
            if(element != -1):
                visited.append(element)
                dfs(tree[element],f + 1)

for i in range(n):
    if(i not in visited and list1[i] == -1):
        visited.append(i)
        dfs(tree[i],0)

print(count)