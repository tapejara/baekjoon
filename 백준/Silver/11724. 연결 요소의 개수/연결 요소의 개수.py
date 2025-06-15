import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int,input().split())
list1 = [[] for _ in range(n)]
list2 = [0 for _ in range(n)]
answer = 0
for i in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    list1[a].append(b)
    list1[b].append(a)
for i in range(n):
    list1[i].sort()
def function(x):
    global answer
    list2[x] = 1
    for element in list1[x]:
        if(list2[element] == 0):
            function(element)
for i in range(n):
    if(list2[i] == 0):
        function(i)
        answer += 1
print(answer)