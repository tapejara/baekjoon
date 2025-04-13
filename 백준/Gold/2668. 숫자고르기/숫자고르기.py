import sys
input = sys.stdin.readline
n = int(input())
list1 = [-1]
for _ in range(n):
    list1.append(int(input()))
visited = []
answer = []
temp = []
flag = 0
def dfs(a):
    temp.append(a)
    if(temp.count(flag) == 2):
        temp.remove(flag)
        for element in temp:
            answer.append(element)
        return
    if(list[a] not in visited):
        visited.append(list[a])
        dfs(list1[a])
        visited.pop()
        temp.pop()

for i in range(n + 1):
    if(i in list1 and i not in answer):
        flag = i
        dfs(i)
        temp.clear()

answer.sort()
print(len(answer))
for eleemnt in answer:
    print(eleemnt)