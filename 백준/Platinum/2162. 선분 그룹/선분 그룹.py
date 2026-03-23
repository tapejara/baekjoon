import sys
input = sys.stdin.readline
def ccw(a,b,x,y,n,m):
    return (a * y + x * m + n * b) - (a * m + x * b + n * y)
def find(x):
    if(board[x] != x):
        return find(board[x])
    else:
        return x
def union(a, b):
    a = find(a)
    b = find(b)
    if(a < b):
        board[b] = a
    else:
        board[a] = b
n = int(input())
list1 = [list(map(int,input().split())) for _ in range(n)]
board = [i for i in range(n)]
score = [0 for _ in range(n)]
for i in range(n):
    w, x, y, z = list1[i]
    for j in range(i + 1, n):
        e, f, g, h = list1[j]
        point1 = ccw(w, x, y, z, e, f) 
        point2 = ccw(w, x, y, z, g, h)
        point3 = ccw(e, f, g, h, w, x)
        point4 = ccw(e, f, g, h, y, z)
        if(point1 * point2 < 0 and point3 * point4 < 0):
            union(i, j)
        elif((point1 * point2 < 0 or point3 * point4 < 0) and (point1 * point2 == 0 or point3 * point4 == 0)):
            if((min(w, y) <= e <= max(w, y) and min(x, z) <= f <= max(x, z)) or
                (min(w, y) <= g <= max(w, y) and min(x, z) <= h <= max(x, z)) or
                (min(e, g) <= w <= max(e, g) and min(f, h) <= x <= max(f, h)) or
                (min(e, g) <= y <= max(e, g) and min(f, h) <= z <= max(f, h))):
                union(i, j)
        elif(point1 * point2 == 0 and point3 * point4 == 0 and 
           ((min(w, y) <= e <= max(w, y) and min(x, z) <= f <= max(x, z)) or
             (min(w, y) <= g <= max(w, y) and min(x, z) <= h <= max(x, z)) or
             (min(e, g) <= w <= max(e, g) and min(f, h) <= x <= max(f, h)) or
             (min(e, g) <= y <= max(e, g) and min(f, h) <= z <= max(f, h)))):
            union(i, j)
answer = 0
for i in range(n):
    if(find(i) == i):
        answer += 1
    score[find(i)] += 1
print(answer)
print(max(score))