n = int(input())
list1 = [[c for c in input()] for _ in range(n)]
x = 0
y = 0
for i in range(n):
    point = 0
    for j in range(n):
        if(list1[i][j] == "."):
            point += 1
        else:
            point = 0
        if(point == 2):
            x += 1
for i in range(n):
    point = 0
    for j in range(n):
        if(list1[j][i] == "."):
            point += 1
        else:
            point = 0
        if(point == 2):
            y += 1
print(x, y)