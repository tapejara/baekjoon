import sys
sys.setrecursionlimit(10**6)
n = int(input())
temp = [0,1]
for i in range(2, n):
    temp.append(temp[i - 1] + i)
tetra = [0,1]
for i in range(2, n):
    if(tetra[-1] >= n):
        break
    tetra.append(tetra[i - 1] + temp[i])
answer = n
def function(x, y, count):
    global answer
    if(x == 0):
        answer = min(count, answer)
    for i in range(y, 0, -1):
        if(x >= tetra[i] and count + 1 < answer):
            function(x - tetra[i], i, count + 1)
function(n, len(tetra) - 1, 0)
print(answer)